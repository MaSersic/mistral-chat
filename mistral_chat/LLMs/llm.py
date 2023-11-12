import os

from langchain.llms import LlamaCpp
from mistral_chat import settings
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

lmm_path = os.path.join(settings.BASE_DIR, 'mistral_chat', 'LLMs', 'openhermes-2.5-mistral-7b.Q8_0.gguf')


class LLM:
    def __init__(self, model_path=lmm_path, n_ctx=16384, max_tokens=200):
        self.llm = llm = LlamaCpp(model_path=model_path, n_ctx=n_ctx, max_tokens=max_tokens)
        memory = ConversationBufferMemory(return_messages=True)
        memory.load_memory_variables({})
        self.conversation = ConversationChain(llm=llm, memory=memory)

    def ask(self, prompt):
        return self.conversation.predict(input=prompt)
