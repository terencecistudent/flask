import os

# Importing flask class
from flask import Flask, render_template

# Creating instance of this and storing in a var called app
# First argument of the Flask class is the name of the applications module
app = Flask(__name__)

# A decorator starts with the @ sign, which is also called pie notation. 
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")

# Name of the default module in Python.
if __name__ == "__main__":
    app.run(host='0.0.0.0', 
            port=5000, 
            debug=True)