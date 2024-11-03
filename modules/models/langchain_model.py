from langchain.chains.question_answering import load_qa_chain
from modules.services.llms.open_ai_service import OpenAiService
from modules.services.vector_databases.pinecone_service import PineconeService

def get_answer(question, document_id):
    llm = OpenAiService.chat_model()
    docs = PineconeService.search_by_query(question, document_id=document_id)

    chain = load_qa_chain(
        llm,
        chain_type="stuff"
    )
    result = chain.run(input_documents=docs, question=question)
    return result
