from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    sent = False
    name = ""
    if request.method == "POST":
        name = request.form.get("name", "")
        sent = True
    return render_template("contact.html", sent=sent, name=name)

@app.route("/student")
def student():
    return "Cloud Computing - PaaS Practical Work"