import os
import json

# Importing flask class
from flask import Flask, render_template, request, flash

# Creating instance of this and storing in a var called app
# First argument of the Flask class is the name of the applications module
app = Flask(__name__)
app.secret_key = "some_secret"

# A decorator starts with the @ sign, which is also called pie notation. 
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}

    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            # if url in that particular element of array is equal to member_name, then member obj should equal our obj
            if obj["url"] == member_name:
                member = obj

    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():    
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
              request.form["name"]))

    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

# Name of the default module in Python.
if __name__ == "__main__":
    app.run(host='0.0.0.0', 
            port=5000, 
            debug=True)