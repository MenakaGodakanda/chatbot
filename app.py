from flask import Flask, render_template, request
from chatbot_logic import Chatbot

# Initialize Flask app and Chatbot
app = Flask(__name__)
chatbot = Chatbot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["user_input"]
    response = chatbot.generate_response(user_input)
    return response

if __name__ == "__main__":
    app.run(debug=True)
