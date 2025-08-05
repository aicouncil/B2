#pip install Flask - to install Flask in the system

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():                      #http://127.0.0.1:5000
    return "<p>Hello, World!</p>"

@app.route("/greet")          #http://127.0.0.1:5000//greet
def greetings():
    return "Welcome to our prediction model"

app.run()
