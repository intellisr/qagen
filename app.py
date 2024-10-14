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
from bson import ObjectId, json_util
import json

app = Flask(__name__)

os.environ["GOOGLE_API_KEY"] = "AIzaSyCcjopgzEHHfNrbSGwrTQvUc91RjUJL-kg"

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
verified_collection = db["verified"]

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
            
def dict_to_html(data):
    html_output = ""
    for key, value in data.items():
        html_output += f'<div class="item">\n'
        html_output += f'    <div class="key">{key}:</div>\n'
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                sub_value_new=str(sub_value)
                sub_value_new2=sub_value_new.replace("[","").replace("[","").replace("'","")
                html_output += f'    <div class="sub-item">\n'
                html_output += f'        <div class="sub-key">{sub_key}:</div>\n'
                html_output += f'        <div class="sub-value">{sub_value_new2}</div>\n\n'
                html_output += f'    </div>\n\n'
        else:
            html_output += f'    <div class="value">{value}</div>\n'
        html_output += f'</div>\n<br/>'
    return html_output

def text_to_html(text):
    html_output = ""
    lines = text.split("Heading:")
    
    for section in lines:
        if section.strip():  # Ignore any empty strings
            parts = section.split('*')
            heading = parts[0].strip()  # Extract heading
            html_output += f'<h3>{heading}</h3>\n'
            
            if len(parts) > 1:
                html_output += "<ul>\n"
                for item in parts[1:]:
                    html_output += f'  <li>{item.strip()}</li>\n'
                html_output += "</ul>\n"
    
    return html_output      
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
        current_files = os.listdir()  # Lists files in the current directory    
        if document_name in current_files:
            print("Doc exist")
        else:
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
            if isinstance(value, dict):
                for key2, value2 in value.items():
                    test_cases,summery = test_case_agent.generate_test_cases({key:{key2:value2}})
                    testcases_collection.insert_one({"document_name": document_name,"requirement":summery ,"test_cases": test_cases})
                    print(f"Test cases saved to MongoDB: {test_cases}")
                    time.sleep(10)
            else:
                test_cases,summery = test_case_agent.generate_test_cases({key:value})
                testcases_collection.insert_one({"document_name": document_name,"requirement":summery ,"test_cases": test_cases})
                print(f"Test cases saved to MongoDB: {test_cases}")
                time.sleep(10)        
            
    test_case_docs = testcases_collection.find({"document_name": document_name})
    documents = list(test_case_docs)
    # Serialize the documents using json_util
    json_docs = json.loads(json_util.dumps(documents))

    # Return the documents in the expected format
    return jsonify({'documents': json_docs})

@app.route('/verify_test_cases', methods=['POST'])
def verify_test_cases():
    data = request.get_json()
    document_id = data['document_id']
    verified_test_cases={}
    req_data = verified_collection.find_one({"document_id": document_id})
    if req_data:
      print(f"Verified document found for {document_id}")
      verified_test_cases=req_data['verified']
    else:
        # Retrieve the document from the database using document_id
        test_case_doc = testcases_collection.find_one({'_id': ObjectId(document_id)})
        test_case = test_case_doc.get("test_cases")
        requirement = test_case_doc.get("requirement")
        test_case_mapping_agent = TestCaseMappingAgent(llm, vector_db, embedding_model)
        verified_test_cases = test_case_mapping_agent.map_requirements_to_test_cases(requirement,test_case)
        verified_collection.insert_one({"document_id": document_id ,"verified": verified_test_cases})
    
    return jsonify({'verified_test_cases': verified_test_cases})

if __name__ == '__main__':
    app.run(debug=True)
