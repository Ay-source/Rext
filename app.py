from flask import Flask, render_template
from database.models import setup

app = Flask(__name__)
"""setup(app)"""


#Route handler for the sign in page
@app.route("/sign_in")
def sign_in():
    return render_template("sign_in.html")

#Handler for the root page
@app.route("/")
def root():
    return render_template("index.html")

"""#Handler for the home page
@app.route("/home")
def home():
    pass

#Handler for the profile page
@app.route()
def route():
    pass

#Handler"""