# COMPLETE END TO END RAG AI APPLICATION

# How to Launch

## Using Docker (Recommended)

Just execute the following two commands:
It may take 15-20 minutes to load but ones done its quick to launch.

```bash
docker pull ghcr.io/shree7676/databaseai-task:latest
docker run -p 5000:5000 ghcr.io/shree7676/databaseai-task:latest
```

## Using the Traditional Approach

1. Clone the repository:
   ```bash
   git clone https://github.com/Shree7676/DataBaseAI_Task.git
   ```
2. Set up a virtual environment: (Optional/Recomended)
   ```bash
   python3 -m venv ai_virtual_env
   source ai_virtual_env/bin/activate
   ```
3. Install the dependencies:
   ```bash
   cd DataBaseAI_Task
   pip install -r requirements.txt
   ```
4. Log in to Hugging Face:
   - [Login Page](https://huggingface.co/login)
   - [Generate API Token](https://huggingface.co/settings/tokens)
5. Create a `.env` file and add the API token:
   ```env
   HUGGINGFACE_API_TOKEN="your_token"
   ```
6. Run the application:
   ```bash
   python3 app.py
   ```

---

# Complete End-to-End Workflow

This project includes the following components:

1. **Extracting a Sample Data**  
2. **Creating a Vector DB**  
3. **Building a RAG App**  
4. **RAG Validation**  
5. **Creating a Frontend**  
6. **Deploying** (Unsuccessful due to extra memory usage)  
7. **Docker**  

---

# Validation Strategy

### Challenges To Overcome:
- The model may **hallucinate insights** that are not supported by the data.  
- It sometimes produces **irrelevant or incoherent summaries**.  
- **Logical inconsistencies** may occur between the feedback and the generated output.  

### Countermeasures that are Implemented:
1. **Using Fine-Tuned LLM**:  
   An LLM fine-tuned to check hallucination helps in identifying responses that are inconsistent with the retrieved data. 
   In the image below you can see that though the second statement can be true in real world we still classify it as hallucination because the content was not present in the retrieved data and it was using the knowledge that it had pre learned.
   ![image](https://github.com/user-attachments/assets/9a606042-b0bb-4380-bc6c-cc0cebb7445c)

   ![image](https://github.com/user-attachments/assets/443fed57-e813-468f-9477-9547bbf76161)


	 While this also seemed to be a tricky response to validation model as in first statement you can see it says “Elon Musk is not mentioned in the context provided.” which is true however it still gets the score of 91% and the only possible reason I think of is because the retrieved content has a data related to Gold Musk.
 

3. **Source Traceability**:  
   Even validation models can fail in certain scenarios. In such cases, passing the source data to the model ensures the generated response remains reliable and accurate and can be cross verified by the end user.

### Additional Approaches for Improved Accuracy:
3. **Using RAG Agents**:  
   Unlike the simple RAG application demonstrated in this project, utilizing a RAG agent can enable multiple models to interact with each other, providing more robust and validated responses. For example, a RAG agent could coordinate between retrieval, summarization, and validation models to ensure accuracy.

4. **Optimized Prompt Design**:  
   I strongly feel the combination of multi modals with specialized prompts have way better chances to provide accurate data.

5. **Data Quality**:  
   This project made me realize the importance of how you pass the data. As you can see its a customer feedback data for products so if you don't add proper metadata for the particular chunks of text in vectordb it may so happen that the the feedbacks of one product may be connected to another.
	 How i overcame it, as in this particular sample data there were hardly few product names and only feedback which makes it hard so while creating the embedding i added the product name with the feedback and then created the embedding plus adding the product name in meta data.

6. **Response History**:  
   Keeping track of responses and user feedback is another crucial step for improving accuracy. This historical context helps refine the model’s output over time by identifying patterns in errors and successes.  

---

# EXPLORING CODE BASE

# Data Exploration (/Data Directory)

The `Data` folder includes the file which helped me to get a sample data below are the brief summary of what each file is. As it was a exploration phase of data so I thought of not adding any comments due to time constraints, However other files have a detailed comments.

- **Amazon Reviews Dataset (2023)**:  
  I used the large-scale Amazon Reviews dataset provided by McAuley Lab ([Dataset Source](https://amazon-reviews-2023.github.io/main.html)).  
  This dataset contains over 571.54M reviews and is about 8GB in size so I just took a sample of data from it.

- **`previous.py`**:  
  This file contains a history of commands and results from the Ipython interactive terminal. Here, I explored the data and extracted a sample small size dataset.

- **`DataBaseAI_task.ipynb`**:  
  This notebook contains preprocessing code. You can view it [here](https://gist.github.com/Shree7676/ec78c49e18445a063d735a61dffb91ec). Since the focus was on reviews and topics, other data like ratings were omitted due to time constraints.

- **`data.json`**:  
  This file contains the final processed data used in the RAG app.  

---

# Vector DB

The `Creating_vector_db.py` script converts `data.json` into vector embeddings and stores them in the VectorDB using the ChromaDB package. The Vector DB is stored in the `vectorDB` directory.  

---

# RAG Application

The `rag_app.py` script creates a RAG application.  
- Behind the scenes, the Mistral-7b LLM model is used.  
- You will need a Hugging Face token to access the model.  (If you proceed with docker you can use my token which is valid uptill 19 Jan)

---

# Flask Frontend

The `app.py` file serves as the entry point for the application.  
- It includes two routes for chatbot interactions.  
- Frontend code is located in the `templates/static` directory.  

---

# Deployment Challenges

1. **Vercel Deployment**:  
   Deployment didn’t succeed because the hallucination fine-tuned model wasn’t available as an API and had to be run locally. While this model isn’t large, it posed challenges for Vercel deployment. If the project only involved the RAG app, deployment would have been straightforward.  

2. **Docker**:  
   As a fallback, I created a Dockerfile for hassle-free deployment.  
   - The published Docker image includes an API key valid for one week for quick testing.  
   - Note: The first-time pull may take 15–20 minutes, so grab a coffee while it loads.  

---

Let me know if any additional details are required or if specific areas need more refinement. 😊
