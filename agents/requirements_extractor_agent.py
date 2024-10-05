from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import ast

class RequirementsExtractorAgent:
    def __init__(self, llm):
        self.llm = llm

    def extract_requirements(self, text):
        prompt_template = """
        You are an expert at extracting software requirements from documents.
        Given the following text from a Software Requirements Specification (SRS), identify and list the main requirements for the software:
        {text}
        List the main requirements clearly and concisely as a python dictionary.
        """
        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
        chain = LLMChain(llm=self.llm, prompt=prompt)
        requirements = chain.run(text)
        return self._parse_requirements(requirements)

    def _parse_requirements(self, requirements_text):
        dict_end = requirements_text.split("= ")[1]
        dict_start = dict_end.replace("```", "")
        return ast.literal_eval(dict_start.strip())
