import os

from langchain.llms import LlamaCpp
from mistral_chat import settings
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import SQLiteVSS
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings

lmm_path = os.path.join(settings.BASE_DIR, 'mistral_chat', 'LLMs', 'openhermes-2.5-mistral-7b.Q8_0.gguf')


class LLM:
    def __init__(self, db_path=None, model_path=lmm_path, n_ctx=16384, max_tokens=200):
        self.llm = llm = LlamaCpp(model_path=model_path, n_ctx=n_ctx, max_tokens=max_tokens)
        memory = ConversationBufferMemory(return_messages=True)
        memory.load_memory_variables({})
        self.conversation = ConversationChain(llm=llm, memory=memory)
        if db_path:
            self.db_path = db_path

    def ask(self, prompt):
        return self.conversation.predict(input=prompt)

    def load_file_from_path(self, path):
        if self.db_path:
            loader = TextLoader(path)
            documents = loader.load()

            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            docs = text_splitter.split_documents(documents)
            texts = [doc.page_content for doc in docs]

            embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
            connection = SQLiteVSS.create_connection(db_file=self.db_path)
            db = SQLiteVSS(table="state_union", embedding=embedding_function, connection=connection)
        else:
            print("Missing database")

    def load_file_from_pdf(self, pdf):
        if self.db_path:
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            docs = text_splitter.split_documents(pdf)
            texts = [doc.page_content for doc in docs]

            embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
            connection = SQLiteVSS.create_connection(db_file=self.db_path)
            db = SQLiteVSS(table="state_union", embedding=embedding_function, connection=connection)
        else:
            print("Missing database")