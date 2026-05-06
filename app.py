from flask import Flask , render_template , jsonify , request
from src.helper import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
from src.helper import download_embedding
import os

app = Flask(__name__)

load_dotenv()

#Api_keys
PINECONE_API_KEY= os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY= os.getenv("OPENAI_API_KEY")

#download OpenAI Embedding
embedding = download_embedding()

#Index_name of the vectorstore
index_name ='medical-chatbot'


docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding
)

retriever = docsearch.as_retriever(search_type ='similarity',search_kwargs={'k':3})

chatmodel = ChatOpenAI(model='gpt-4o')
prompt = ChatPromptTemplate.from_messages(
    [
        ('system',system_prompt),
        ('human','{input}'),
    ]
)

question_answer_chain = create_stuff_documents_chain(chatmodel,prompt)
ragchain = create_retrieval_chain(retriever,question_answer_chain)



@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/get' ,methods =['GET','POST'])
def chat():
    msg = request.form['msg']
    input=msg
    print(input)
    response = ragchain.invoke({'input':msg})
    print('response :',response['answer'])
    return str(response['answer'])










if __name__=='__main__':
    app.run(host='0.0.0.0',port =8080,debug=True)