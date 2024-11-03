from pinecone import Pinecone
from flask import current_app
from langchain.schema import Document
from modules.services.llms.open_ai_service import OpenAiService
import uuid


class PineconeService:
    _client = None
    _db_index = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = Pinecone(api_key=current_app.config['PINECONE_API_KEY'])
        return cls._client

    @classmethod
    def index(cls):
        if cls._db_index is None:
            cls._db_index = cls.get_client().Index(current_app.config['PINECONE_INDEX'])
        return cls._db_index

    @classmethod
    def create_vector_store(cls, text_chunks, document_id):
        if cls.is_document_already_inserted(document_id):
            return cls.index()

        embeddings = OpenAiService.embedding_model()
        vectors = embeddings.embed_documents(text_chunks)
        ids = [str(uuid.uuid4()) for _ in vectors]

        vectors_with_metadata = [
            {"id": id_, "values": vector, "metadata": {"text": chunk}}
            for id_, vector, chunk in zip(ids, vectors, text_chunks)
        ]
        cls.index().upsert(namespace=document_id, vectors=vectors_with_metadata)
        return cls.index()

    @classmethod
    def is_document_already_inserted(cls, document_id):
        query_vector = [0] * 1536

        response = cls.index().query(
            namespace=document_id,
            vector=query_vector,
            top_k=1,
        )
        return bool(response['matches'])

    @classmethod
    def search_by_query(cls, query, document_id):
        embeddings = OpenAiService.embedding_model()
        query_vector = embeddings.embed_query(query)

        response = cls.index().query(
            namespace=document_id,
            vector=query_vector,
            top_k=5,
            include_metadata=True
        )

        return [Document(page_content=match['metadata']['text']) for match in response['matches']]
