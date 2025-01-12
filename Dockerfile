# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install nltk and download the 'punkt_tab' resource
RUN python -m nltk.downloader punkt_tab

# Copy all files from the current directory to the container's /app directory
COPY . .

# Expose the port your Flask app runs on
EXPOSE 5000

# Command to run the Flask app
CMD ["python3", "app.py"]
