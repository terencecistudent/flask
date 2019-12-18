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

# Name of the default module in Python.
if __name__ == "__main__":
    app.run(host='0.0.0.0', 
            port=5000, 
            debug=True)