from langchain_community.chat_models import ChatOpenAI, ChatOllama
from typing import Optional

import os


class ChatOpenRouter(ChatOpenAI):
    openai_api_base: str
    openai_api_key: str
    model_name: str

    def __init__(
        self,
        model_name: str,
        openai_api_key: Optional[str] = None,
        openai_api_base: str = "https://openrouter.ai/api/v1",
        **kwargs
    ):
        openai_api_key = openai_api_key or os.getenv("OPENROUTER_API_KEY")
        super().__init__(
            openai_api_base=openai_api_base,
            openai_api_key=openai_api_key,
            model_name=model_name,
            **kwargs
        )


# class ollama(ChatOllama):
#     llm: any

#     def __init__(
#         self,
#         model_name: str,
#         **kwargs
#     ):
#         self.llm = ChatOllama(model_name=model_name, **kwargs)
