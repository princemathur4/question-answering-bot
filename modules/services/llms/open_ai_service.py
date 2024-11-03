from langchain_community.embeddings import OpenAIEmbeddings
from flask import current_app
from langchain_community.llms import OpenAI


class OpenAiService:

    @classmethod
    def embedding_model(cls):
        return OpenAIEmbeddings(model=current_app.config['OPENAI_EMBEDDINGS_MODEL'],
                                api_key=current_app.config['OPENAI_API_KEY'])

    @classmethod
    def chat_model(cls):
        return OpenAI(
            temperature=0,
            api_key=current_app.config['OPENAI_API_KEY']
        )
