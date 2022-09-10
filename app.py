from flask import Flask, render_template, request
from database.models import setup
from auth import check_login

app = Flask(__name__)
"""setup(app)"""


#Route handler for the sign in page
@app.route("/sign_in", methods=["GET","POST"])
def sign_in():
    if request.method == "POST":
        check_login()
    return render_template("sign_in.html")

@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")

#Handler for the root page
@app.route("/")
def root():
    return render_template("index.html")

#Handler for the home page
@app.route("/home")
def home():
    pass

"""
#Handler for the profile page
@app.route()
def route():
    pass

#Handler"""