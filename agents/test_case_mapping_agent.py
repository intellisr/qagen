from agents.test_case_generator_agent import TestCaseGeneratorAgent
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

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
        if not query_result['matches']:
            return False, "Requirement not found in SRS document."

        best_match = query_result['matches'][0]
        similarity_score = best_match['score']

        # Assuming a similarity score threshold for correctness
        if similarity_score < 0.5:
            return False, f"Requirement is incorrect or does not match the SRS document closely enough (similarity score: {similarity_score})."

        return True, best_match

    def check_test_case_coverage(self, requirement_embedding, test_cases):
        relevant_test_cases = []
        for test_case in test_cases:
            test_case_text = f"{test_case.get('description', '')} {test_case.get('steps', '')} {test_case.get('expected_result', '')}"
            test_case_embedding = self.embedding_model.embed_documents([test_case_text])[0]
            similarity = self.compute_similarity(requirement_embedding, test_case_embedding)
            print(similarity)
            if similarity > 0.2:
                relevant_test_cases.append({
                    "test_case": test_case,
                    "similarity": similarity
                })      
        has_enough_test_cases = len(relevant_test_cases) >= len(test_cases)/4
        return has_enough_test_cases, relevant_test_cases

    def extract_test_case_text(self, test_cases_list):
        texts = []
        for tc_content in test_cases_list:
            description = tc_content.get('description', '')
            steps = tc_content.get('steps', '')
            expected_result = tc_content.get('expected_result', '')
            combined_text = f"{description} {steps} {expected_result}"
            texts.append(combined_text)
        return ' '.join(texts)

    def parse_requirements(self, requirement_text):
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

    def map_requirements_to_test_cases(self, requirement_text, test_cases):
        result_dict = {}
        requirements_dict = self.parse_requirements(requirement_text)

        for heading, requirements in requirements_dict.items():
            for req in requirements:
                req_key = heading
                req_value = req
                combined_requirement = f"{heading}: {req}"
                print(f"Processing requirement: {combined_requirement}")

                is_correct, feedback = self.verify_requirement(combined_requirement)

                if is_correct:
                    requirement_embedding = self.embedding_model.embed_documents([combined_requirement])[0]
                    has_enough, relevant_test_cases = self.check_test_case_coverage(requirement_embedding, test_cases)

                    if has_enough:
                        result_dict[combined_requirement] = {
                            "status": "Requirement is correct and has sufficient relevant test cases.",
                            "test_cases": [tc['test_case'] for tc in relevant_test_cases]
                        }
                    else:
                        test_case_agent = TestCaseGeneratorAgent(self.llm)
                        new_test_cases, _ = test_case_agent.generate_test_cases({req_key: [req_value]})
                        result_dict[combined_requirement] = {
                            "status": "Not enough relevant test cases found; generated new test cases.",
                            "test_cases": new_test_cases
                        }
                else:
                    result_dict[combined_requirement] = {
                        "status": "Requirement is incorrect.",
                        "feedback": feedback
                    }

        return result_dict

    def compute_similarity(self, embedding1, embedding2):
        # Ensure embeddings are 2D arrays
        embedding1 = np.array(embedding1).reshape(1, -1)
        embedding2 = np.array(embedding2).reshape(1, -1)
        # Compute cosine similarity
        similarity = cosine_similarity(embedding1, embedding2)[0][0]
        return similarity