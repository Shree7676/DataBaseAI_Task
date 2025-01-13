import torch
from transformers import AutoModelForSequenceClassification
import spacy

model = AutoModelForSequenceClassification.from_pretrained(
    "vectara/hallucination_evaluation_model", trust_remote_code=True
)

# Initialize spaCy blank model and add the sentencizer
nlp = spacy.blank("en")
nlp.add_pipe("sentencizer")

def simplify_statements(answer_text):
    doc = nlp(answer_text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

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
