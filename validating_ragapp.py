import torch
from transformers import AutoModelForSequenceClassification
import spacy

# Fine tuned llm model which evaluates the hallucination in a response.
model = AutoModelForSequenceClassification.from_pretrained(
    "vectara/hallucination_evaluation_model", trust_remote_code=True
)

# Spcay is required to break the response into simple statements
nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")

def simplify_statements(answer_text):
    doc = nlp(answer_text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

# pairs is a list of tuple, 
# In each tuple the retrived data and the sentence is present.
def get_predictions(pairs):
    outputs = model.predict(pairs)
    predictions = outputs
    return predictions

if __name__ == "__main__":

    context = "Capital of India is New Delhi. Elon is the leading business tycoon in the world"
    answer = "Capital of India is Delhi. Musk is Number 1 business man"

    statements = simplify_statements(answer)
    pairs = [(context, statement) for statement in statements]
    predictions = get_predictions(pairs)

    for pair, pred in zip(pairs, predictions):
        print(f"Statement: {pair[1]}")
        print(f"Accuracy: {pred}")
