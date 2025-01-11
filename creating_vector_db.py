import chromadb
import json
from chromadb.utils import embedding_functions


chroma_client = chromadb.PersistentClient(path="vectorDB")

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")


collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function=sentence_transformer_ef)

data_path = './Data/data.json'

with open(data_path, 'r') as file:
    products_data = json.load(file)

documents = []  # This will hold product reviews
metadatas = []  # This will hold associated metadata (like product names)
ids=[]

for product_name, review in products_data.items():
    review.insert(0,product_name)
    documents.append(str(review))  # Store the review text (can store just product name if needed)
    metadatas.append({"product_name": product_name})  # Metadata with product name and review
    ids.append(product_name)  # Use the product name or a unique ID as the document ID


collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)