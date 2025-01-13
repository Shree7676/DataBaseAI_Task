from chromadb.utils import embedding_functions
from huggingface_hub import InferenceClient
import chromadb
import os
from dotenv import load_dotenv

from validating_ragapp import simplify_statements, get_predictions

load_dotenv()

# Loading LLM Model
model_id = "mistralai/Mistral-7B-Instruct-v0.2"
api_token = os.getenv('HUGGINGFACE_API_TOKEN')
client = InferenceClient(model=model_id, token=api_token)

# Connecting to the vectorDB with respective embedding function used while creating vectorDB
chroma_client = chromadb.PersistentClient(path="vectorDB")
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")
collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function=sentence_transformer_ef)

# Retriving respective data from vectorDB based on query
def query_vector_db(query, top_k=3):
    results = collection.query(
        query_texts=[query],
        n_results=top_k
    )
    return results  

# Connecting llm, passing the retrived data and question to the model.
def ask_question_with_context(question, top_k=3):
    retrived_data = query_vector_db(question, top_k=top_k)
    prompt = f"""
You are an assistant. Use the following context to answer the question accurately and concisely.

Context:
{retrived_data}

Question: {question}
Answer:
"""
    response = client.text_generation(
        prompt,
        max_new_tokens=1024,
        temperature=0.1,
        repetition_penalty=1.2
    )

    # Splitting each sentence and predecting if its present in retrieved data
    statements = simplify_statements(response)
    pairs = [(retrived_data, statement) for statement in statements]
    predictions = get_predictions(pairs)
    # Combining the sentence and its predection to display in front end.
    validation = zip(pairs, predictions)
    return response , retrived_data['documents'], validation

if __name__=="__main__":
    question = "whats the review of Black Eye Patch with Tie Band"
    response, retrived_data, validation = ask_question_with_context(question)
    print("Model Response:", response)
