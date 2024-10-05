from agents.test_case_generator_agent import TestCaseGeneratorAgent

# Agent 4: TestCaseMappingAgent
class TestCaseMappingAgent:
    def __init__(self, llm, vector_db, embedding_model):
        self.llm = llm
        self.vector_db = vector_db
        self.embedding_model = embedding_model

    def verify_requirement(self, requirement_text):
        requirement_embedding = self.embedding_model.embed_documents([requirement_text])[0]
        query_result = self.vector_db.query(
            vector=requirement_embedding,
            top_k=5,
            include_values=False,
            include_metadata=True
        )
        is_present = any(result['score'] > 0.85 for result in query_result['matches'])
        return is_present, query_result['matches']

    def check_test_case_coverage(self, requirement_embedding):
        query_result = self.vector_db.query(
            vector=requirement_embedding,
            top_k=10,
            include_values=False,
            include_metadata=True
        )
        has_enough_test_cases = len(query_result['matches']) >= 3
        return has_enough_test_cases, query_result['matches']

    def extract_test_case_text(self,test_cases_dict):
        texts = []
        for tc_id, tc_content in test_cases_dict.items():
            description = tc_content.get('description', '')
            preconditions = tc_content.get('preconditions', '')
            steps = ' '.join(tc_content.get('steps', []))
            expected_result = tc_content.get('expected_result', '')
            combined_text = f"{description} {preconditions} {steps} {expected_result}"
            texts.append(combined_text)
        return ' '.join(texts)

    def parse_requirements(self,requirement_text):
      requirements_dict = {}
      current_heading = None
      lines = requirement_text.split('\n')
      for line in lines:
          line = line.strip()
          if line.startswith('Heading:'):
              # Extract heading
              current_heading = line.replace('Heading:', '').strip()
              requirements_dict[current_heading] = []
          elif line.startswith('*') and current_heading:
              # Extract bullet point under current heading
              requirement = line.replace('*', '').strip()
              requirements_dict[current_heading].append(requirement)
      return requirements_dict      

    def map_requirements_to_test_cases(self, requirement_text):
        result_dict = {}
        requirements_dict = self.parse_requirements(requirement_text)

        for heading, requirements in requirements_dict.items():
            for req in requirements:
                req_key = heading
                req_value = req
                combined_requirement = f"{heading}: {req}"

                is_present, similar_requirements = self.verify_requirement(combined_requirement)

                if is_present and similar_requirements:
                    similar_id = similar_requirements[0]['id']
                    fetch_result = self.vector_db.fetch(ids=[similar_id], include_values=True)
                    best_match_embedding = fetch_result['vectors'][similar_id]['values']

                    has_enough_test_cases, matching_test_cases = self.check_test_case_coverage(best_match_embedding)

                    if has_enough_test_cases:
                        result_dict[combined_requirement] = {
                            "status": "Requirement found and sufficient test cases available",
                            "test_cases": matching_test_cases
                        }
                    else:
                        test_case_agent = TestCaseGeneratorAgent(self.llm)
                        new_test_cases, _ = test_case_agent.generate_test_cases({req_key: [req_value]})
                        new_test_case_embedding = self.embedding_model.embed_query(new_test_cases)
                        has_enough_test_cases, _ = self.check_test_case_coverage(new_test_case_embedding)

                        result_dict[combined_requirement] = {
                            "status": "New test cases generated",
                            "test_cases": new_test_cases
                        }
                else:
                    test_case_agent = TestCaseGeneratorAgent(self.llm)
                    new_test_cases, _ = test_case_agent.generate_test_cases({req_key: [req_value]})
                    new_test_cases_text = self.extract_test_case_text(new_test_cases)
                    new_test_case_embedding = self.embedding_model.embed_query(new_test_cases_text)
                    has_enough_test_cases, _ = self.check_test_case_coverage(new_test_case_embedding)

                    result_dict[combined_requirement] = {
                        "status": "Requirement not found, new test cases generated",
                        "test_cases": new_test_cases
                    }

        return result_dict