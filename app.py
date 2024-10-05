from flask import Flask, render_template, request, redirect, url_for, jsonify
from agents.srs_loader_agent import SRSLoaderAgent
from agents.requirements_extractor_agent import RequirementsExtractorAgent
from agents.test_case_generator_agent import TestCaseGeneratorAgent
from agents.test_case_mapping_agent import TestCaseMappingAgent
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from pymongo import MongoClient
from pinecone import Pinecone, ServerlessSpec
import os
import time


app = Flask(__name__)

os.environ["GOOGLE_API_KEY"] = "AIzaSyCAm2SkrWVol2gKNeExNlLQJPX9rHZ-bjA"

# Initialize the Gemini model for LLM tasks
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Initialize HuggingFace embeddings and FAISS as vector store
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

pc = Pinecone(api_key="86a3570b-1782-4e25-91c3-2dd516bb3965")

index_name = "srs-docs"

# Check if index exists, if not, create one
if not pc.has_index(index_name):
  pc.create_index(
      name=index_name,
      dimension=len(embedding_model.embed_query("QA_test")),
      metric="cosine",
      spec=ServerlessSpec(
          cloud="aws",
          region="us-east-1"
      )
  )

# Wait for the index to be ready
while not pc.describe_index(index_name).status['ready']:
    time.sleep(1)

vector_db = pc.Index(index_name)

# Initialize MongoDB client
mongo_uri = "mongodb+srv://intelli_test:srgsliit123@testcluster.xm1be.mongodb.net/?retryWrites=true&w=majority&appName=TestCluster"
client = MongoClient(mongo_uri)
db = client.get_database("TestCluster")
doc_collection = db["document"]
requirements_collection = db["requirements"]
testcases_collection = db["testcases"]

# Function to add embeddings to Pinecone
def add_embeddings(document_name):
    doc_data = doc_collection.find_one({"document_name": document_name})
    srs_text = doc_data["doc"]
    sentences = srs_text.split('\n')

    # Embed each sentence and add to Pinecone
    for idx, sentence in enumerate(sentences):
        sentence = sentence.strip()
        if sentence != "":
            embedding = embedding_model.embed_query(sentence)
            # Upsert the vector with ID, values, and optional metadata
            vector_db.upsert(vectors=[{
                'id': f"{document_name}_{idx}",  # Unique ID for each sentence
                'values': embedding,
                'metadata': {'text': sentence}
            }])
      
# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file:
        document_name = file.filename
        file.save(document_name)

    # Find the document in the 'testcases' collection
    doc_data = doc_collection.find_one({"document_name": document_name})
    if doc_data:
        print(f"Data found for {document_name}")
    else:
        srs_agent = SRSLoaderAgent(document_name)
        srs_text = srs_agent.load_and_extract_text()
        proccessed_doc=""
        split_doc=srs_text.split("\n")
        for i in range(len(split_doc)):
            if split_doc[i].strip() != "":
              proccessed_doc+="\n"+split_doc[i].strip()

        doc_collection.insert_one({"document_name": document_name, "doc": proccessed_doc})
        # Add document as embedding into vector database
        add_embeddings(document_name)
    print("Document extacted")
    doc_data = doc_collection.find_one({"document_name": document_name})
    srs_text=doc_data["doc"]
    
    #-------------------------------------------------------------------------------------------

    req_data = requirements_collection.find_one({"document_name": document_name})
    if req_data:
      print(f"Requirenment found for {document_name}")
    else:
      # Agent 2: Extract Requirements
      req_agent = RequirementsExtractorAgent(llm)
      requirements_dict = req_agent.extract_requirements(srs_text)
      requirements_collection.insert_one({"document_name": document_name, "requirements": requirements_dict})

    print("Requirement extacted")
    req_data = requirements_collection.find_one({"document_name": document_name})
    requirements_dict=req_data["requirements"]
    #-------------------------------------------------------------------------------------------

    test_case_doc = testcases_collection.find_one({"document_name": document_name})
    if test_case_doc:
        print(f"Test cases found for {document_name}")
    else:
        # Agent 3: Generate Test Cases
        test_case_agent = TestCaseGeneratorAgent(llm)
        for key, value in requirements_dict.items():
            test_cases,summery = test_case_agent.generate_test_cases(value)
            testcases_collection.insert_one({"document_name": document_name,"requirement":summery ,"test_cases": test_cases})
            print(f"Test cases saved to MongoDB: {test_cases}")
    test_case_docs = testcases_collection.find({"document_name": document_name})
    #-------------------------------------------------------------------------------------------
    if len(test_case_doc) > 3:
      # Agent 4: Testcase Verification and regeneration
      test_case_mapping_agent = TestCaseMappingAgent(llm, vector_db, embedding_model)
      # Map and generate/verify test cases for each requirement using the TestCaseMappingAgent
      for test_case_doc in test_case_docs:
        # Access the test cases from the document
        test_cases = test_case_doc.get("test_cases")
        requirement = test_case_doc.get("requirement")
        verified_test_cases = test_case_mapping_agent.map_requirements_to_test_cases(requirement)
        print(verified_test_cases)

        return jsonify({
            'requirements': requirements_dict,
            'test_cases': test_cases
        })
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
