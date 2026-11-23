from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to my first Azure PaaS application!"

@app.route("/student")
def student():
    return "Cloud Computing - PaaS Practical Work"