from flask import Flask, render_template, request, redirect, url_for, flash
from database.models import setup
from auth import check_login, valsave_credentials

app = Flask(__name__)
setup(app)


#Route handler for the sign in page
@app.route("/sign_in", methods=["GET","POST"])
def sign_in():
    if request.method == "POST":
        check_login()
    return render_template("sign_in.html")

@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        check_login()
        flash("You're Registered!")
        redirect(url_for("root"))
    return render_template("sign_up.html", range=range, permissions=["sell:books", "read:books"])

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