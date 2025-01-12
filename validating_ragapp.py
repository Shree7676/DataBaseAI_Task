import torch
from transformers import AutoModelForSequenceClassification
import nltk
from nltk.tokenize import sent_tokenize

model = AutoModelForSequenceClassification.from_pretrained(
    "vectara/hallucination_evaluation_model",trust_remote_code=True)


def simplify_statements(answer_text):
    sentences = sent_tokenize(answer_text)
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
