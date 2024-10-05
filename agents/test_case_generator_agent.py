from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import ast

# Agent 3: Test Case Generator Agent
class TestCaseGeneratorAgent:
    def __init__(self, llm):
        self.llm = llm

    def generate_test_cases(self, requirements_dict):
        summary = self._create_string_doc(requirements_dict)
        prompt_template = """
        You are an expert in generating test cases from requirements.

        Given the following text from a requirements document, generate a set of test cases that thoroughly cover the provided requirements.

        Please format the test cases as a Python Dictionary, with each test case clearly and concisely described.

        Input Requirements:

        {text}

        Output:

        Python Dictionary of Test Cases:
        """
        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = LLMChain(llm=self.llm, prompt=prompt)
        test_cases = chain.run(summary)
        test_dict=self._parse_testcases(test_cases)
        if type(test_dict)==dict:
          return test_dict,summary
        else:
          print("Retrying to generated test case from:"+summary)
          self.generate_test_cases(requirements_dict)


    def _create_string_doc(self, dict_main, m_str=""):
        if isinstance(dict_main, dict):
          for key, value in dict_main.items():
              m_str += "Heading: " + key + "\n"
              if isinstance(value, dict):
                  m_str = self._create_string_doc(value, m_str)
              else:
                  for val in value:
                      m_str += "      *" + val + "\n"
        else:
          for val in dict_main:
              m_str += "      *" + val + "\n"

        return m_str

    def _parse_testcases(self, requirements_text):
        test_dict={}
        try:
          dict_end = requirements_text.split("= ")[1]
          dict_start = dict_end.replace("```", "")
          print(dict_start.strip())
          test_dict=ast.literal_eval(dict_start.strip())
        except Exception as e:
          print(f"Failed to parse test cases: {e}")
        return test_dict
