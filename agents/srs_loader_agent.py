from langchain_community.document_loaders import PyPDFLoader
import docx  # To handle Word documents
import os

# Agent 1: SRS Loader and Text Extractor
class SRSLoaderAgent:
    def __init__(self, file_path):
        self.file_path = file_path
        self.pages = None

    def load_and_extract_text(self):
        file_extension = os.path.splitext(self.file_path)[1].lower()

        if file_extension == '.pdf':
            self.loader = PyPDFLoader(self.file_path)
            self.pages = self.loader.load()
            text = "".join([page.page_content for page in self.pages])

        elif file_extension == '.docx':
            text = self._extract_text_from_docx()

        else:
            raise ValueError(f"Unsupported file format: {file_extension}")

        return text

    def _extract_text_from_docx(self):
        doc = docx.Document(self.file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        return "\n".join(full_text)
