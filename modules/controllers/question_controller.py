import json
from modules.models.langchain_model import get_answer
from modules.services.vector_databases.pinecone_service import PineconeService
from langchain.text_splitter import RecursiveCharacterTextSplitter
from modules.services.text_extractors.ocr_my_pdf_service import process_pdf_text
from modules.common.utils import get_unique_hash


class QuestionController:
    def process_for_answers(self, document_file, questions_file):
        # Parse questions and document content

        document_bytes = document_file.read()
        document_id = get_unique_hash(document_bytes)
        document_content = process_pdf_text(document_bytes)

        # Split document into chunks and create a vector store in Pinecone
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_text(document_content)

        PineconeService.create_vector_store(text_chunks=chunks, document_id=document_id)

        # Process each question
        output = []
        questions = self.parse_questions(questions_file)
        for question in questions:
            answer = get_answer(question=question, document_id=document_id)
            output.append({"question": question, "answer": answer})
        return output

    @staticmethod
    def parse_questions(questions_file) -> list:
        return json.load(questions_file)
