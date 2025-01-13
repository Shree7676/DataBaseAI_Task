import chromadb
import json
from chromadb.utils import embedding_functions

# Creating vectorDB using chroma at a given locaiton
chroma_client = chromadb.PersistentClient(path="vectorDB")

# This will help to create a sentence into numerical vectors
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

# creates a collection for vectordb
collection = chroma_client.get_or_create_collection(name="my_collection", embedding_function=sentence_transformer_ef)

data_path = './Data/data.json'

with open(data_path, 'r') as file:
    products_data = json.load(file)

documents = []
metadatas = []
ids=[]

# Iterating through raw data and adding it into respective list
for product_name, review in products_data.items():
    review.insert(0,product_name)
    documents.append(str(review))  # Store the review text (can store just product name if needed)
    metadatas.append({"product_name": product_name})  # Metadata with product name and review
    ids.append(product_name)  # Use the product name or a unique ID as the document ID

# Inserting the data into vectorDB, Embedding will happen internally 
# as we have already mentioned type of embedding in line number 9.
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)