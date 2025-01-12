from chromadb.utils import embedding_functions
from huggingface_hub import InferenceClient
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

model_id = "mistralai/Mistral-7B-Instruct-v0.2"
api_token = os.getenv('HUGGINGFACE_API_TOKEN')
client = InferenceClient(model=model_id, token=api_token)

chroma_client = chromadb.PersistentClient(path="vectorDB")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")
collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function=sentence_transformer_ef)

def query_vector_db(query, top_k=3):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    return results  


def ask_question_with_context(question, top_k=3):
    results = query_vector_db(question, top_k=top_k)
    prompt = f"""
You are an assistant. Use the following context to answer the question accurately and concisely.

Context:
{results}

Question: {question}
Answer:
"""
    response = client.text_generation(
        prompt,
        max_new_tokens=1024,
        temperature=0.1,
        repetition_penalty=1.2
    )
    return response

question = "which is the best product"
response = ask_question_with_context(question)
print("Model Response:", response)
