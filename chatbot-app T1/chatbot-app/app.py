
from flask import Flask, render_template, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections

# Sample chatbot pairs
pairs = [
    [r"hi|hello", ["Hello!", "Hi there!"]],
    [r"how are you?", ["I'm doing good!", "Great! How can I help you?"]],
    [r"(.*) your name?", ["I'm a simple chatbot created by Megha."]],
    [r"quit", ["Bye! Take care."]],
    [r"(.*)", ["Sorry, I didn't understand that."]]
]

app = Flask(__name__)
chatbot = Chat(pairs, reflections)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]
    response = chatbot.respond(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    nltk.download('punkt')
    app.run(debug=True)
