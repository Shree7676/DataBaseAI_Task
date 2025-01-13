from flask import Flask, render_template, request, jsonify, redirect,url_for
from rag_app import ask_question_with_context

app = Flask(__name__)

# To store the conversation between bot and user
user_messages = []

# Initial route.
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", user_messages=user_messages)

@app.route("/chat", methods=["POST"])
def chat():
    # Getting response from frontend.
    user_message = request.form["question"]
    user_messages.append((user_message, 'user')) # storing the conversation
    # Passing the response to model.
    bot_response,retrived_data,validation  = ask_question_with_context(user_message)
    user_messages.append((bot_response, 'bot'))
    # Passing the sentence and its prediction to front end.
    validation_output = []
    for pair, pred in validation:
        validation_output.append((pair[1],int(float(pred)*100)))

    return render_template("index.html", user_messages=user_messages,retrived_data=str(retrived_data), validation_output=validation_output )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)