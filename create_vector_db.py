import json
from sentence_transformers import SentenceTransformer
from langchain_community.vectorstores import Chroma
import time

# Load your JSON file (replace with the actual path)
json_path = './Data/data.json'

# Initialize the embedding model (you can choose any Sentence-BERT model)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize a Chroma vector store
persist_directory = './vectorDB'  # specify your directory
db_chroma = Chroma(persist_directory=persist_directory)

# Read the JSON file
with open(json_path, 'r') as file:
    products_data = json.load(file)

# List to hold all the embeddings and metadata
documents = []  # This will hold product reviews
metadatas = []  # This will hold associated metadata (like product names)
embeddings = []
ids = []  # Optional: You can store product IDs or unique identifiers if needed

# Start embedding generation
start_time = time.time()

for product_name, review in products_data.items():
    # Create the text to embed (You can concatenate the product name with its review if needed)
    text_to_embed = f"{product_name}: {review}"
    
    # Generate embedding for the text
    embedding = embedding_model.encode(text_to_embed)
    
    # Store the text and its corresponding embedding in the vector store
    documents.append(text_to_embed)  # Store the review text (can store just product name if needed)
    metadatas.append({"product_name": product_name})  # Metadata with product name and review
    embeddings.append(embedding)
    ids.append(product_name)  # Use the product name or a unique ID as the document ID

# Add all the documents and embeddings to the vector store
db_chroma.add_documents(documents, embeddings, metadatas, ids)

# Optionally, persist the vector store
db_chroma.persist()

# Print the time it took
end_time = time.time()
print(f"Time taken to process and store embeddings: {end_time - start_time} seconds.")

print(f"Vector store built and stored at {persist_directory}")
