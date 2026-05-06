from langchain.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from typing import List
from langchain.schema import Document
import os


#Extract Data from the PDF file
def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()
    return documents


#Filter desired context in document 
def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    """
    Given a list of Document objects, return a new list of Document objects
    containing only 'source' in metadata and the original page_content.
    """
    minimal_docs: List[Document] = []
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src}
            )
        )
    return minimal_docs

#Split the Data into Text Chunks
def text_split(minimal_docs):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks=text_splitter.split_documents(minimal_docs)
    return text_chunks

#Download the Embedding model
def download_embedding():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        dimensions=256,
        openai_api_key= os.getenv("OPENAI_API_KEY")
    )

    return embeddings