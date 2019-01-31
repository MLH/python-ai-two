from flask import Flask, render_template
from flask_socketio import SocketIO
from markov_bot import generate_bot_answer
import json
import config

app = Flask(__name__)
socketio = SocketIO(app)


# Renders UI
@app.route("/")
def home():
    return render_template("homepage.html")

# Chat API - WebSocket
@socketio.on("send question")
def generate_message(body, methods=["POST"]):
    
    

    try:
       
       
       
    except:
       
       
       

if __name__ == "__main__":
    socketio.run(app)
