from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
import ast
import json

# Agent 3: Test Case Generator Agent
class TestCaseGeneratorAgent:
    def __init__(self, llm):
        self.llm = llm

        # Define response schemas
        response_schemas = [
            ResponseSchema(name="test_case_id", description="A unique identifier for the test case."),
            ResponseSchema(name="description", description="A clear and concise description of the test case."),
            ResponseSchema(name="steps", description="Detailed steps to execute the test."),
            ResponseSchema(name="expected_result", description="The expected result after performing the test.")
        ]

        # Create the Structured Output Parser
        self.output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
        format_instructions = self.output_parser.get_format_instructions()

        # Define the prompt template
        prompt_template = """
        You are an expert in generating test cases from requirements.

        Given the following text from a requirements document, generate a set of test cases that thoroughly cover the provided requirements.

        Please format the test cases as a JSON array where each test case matches the following schema:

        {format_instructions}

        Input Requirements:

        {text}

        Output:

        JSON array of Test Cases:
        """

        self.prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["text"],
            partial_variables={"format_instructions": format_instructions}
        )

        self.chain = LLMChain(
            llm=self.llm,
            prompt=self.prompt,
            # output_parser=self.output_parser
        )

    def generate_test_cases(self, requirements_dict):
        summary = self._create_string_doc(requirements_dict)
        test_cases_output = self.chain.run(summary)
        # print("Raw Output from LLM:", test_cases_output)
        # Attempt to parse the output directly, using a more flexible approach
        try:
            
            # Extract the JSON part manually (if needed)
            json_start = test_cases_output.find("[")
            json_end = test_cases_output.rfind("]") + 1
            if json_start != -1 and json_end != -1:
                json_output = test_cases_output[json_start:json_end]
                test_cases = json.loads(json_output)
                return test_cases, summary
            else:
                print("Failed to find valid JSON structure in the output.")
                return None, summary
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")
            return None, summary

    def _create_string_doc(self, dict_main, m_str=""):
        if isinstance(dict_main, dict):
            for key, value in dict_main.items():
                m_str += "Heading: " + key + "\n"
                if isinstance(value, dict):
                    m_str = self._create_string_doc(value, m_str)
                else:
                    if isinstance(value, str):
                       m_str += "      * " + value + "\n"
                    else:  
                      for val in value:
                          if isinstance(val, dict):
                            m_str = self._create_string_doc(val, m_str)
                          else:  
                            m_str += "      * " + val + "\n"
        else:
            for val in dict_main:
                m_str += "      * " + val + "\n"

        return m_str
