from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import ast
import json

# Agent: Requirements Extractor Agent
class RequirementsExtractorAgent:
    def __init__(self, llm):
        self.llm = llm

        # Define the prompt template
        prompt_template = """
        You are an expert at extracting software requirements from documents.

        Given the following text from a Software Requirements Specification (SRS), identify and list the main requirements for the software.

        Organize the requirements into a hierarchical JSON structure with the following format:

        {{
            "Functional Requirements": {{
                "Subcategory1": [
                    "Requirement1",
                    "Requirement2",
                    ...
                ],
                "Subcategory2": [
                    ...
                ],
                ...
            }},
            "Non Functional Requirements": {{
                ...
            }},
            "GUI Requirements": {{
                ...
            }},
            "Performance Requirements": {{
                ...
            }},
            "Security Requirements": {{
                ...
            }}
            ...
        }}

        Please ensure that the output JSON strictly follows this format, filling in the relevant requirements under appropriate categories and subcategories based on the input text.

        Input Text:

        {text}

        Output:

        JSON object of Requirements:
"""

        self.prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["text"]
        )

        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt
        )

    def extract_requirements(self, text):
        requirements_output = self.chain.run(text)
        # Attempt to parse the output directly
        try:
            # Extract the JSON part manually
            json_start = requirements_output.find("{")
            json_end = requirements_output.rfind("}") + 1
            if json_start != -1 and json_end != -1:
                json_output = requirements_output[json_start:json_end]
                requirements = json.loads(json_output)
                return requirements
            else:
                print("Failed to find valid JSON structure in the output.")
                return None
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")
            return None
