from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
from database.models import setup, User as Users
from auth import check_login, valsave_credentials
from forms import User, Books, username_valid

app = Flask(__name__)
setup(app)
Session(app)


def check_session():
    try:
        if session['name']:
            return True
        else:
            return False
    except:
        return False



#Route handler for the sign in page
@app.route("/sign_in")
def sign_in():
    form = User()
    username=request.args.get("username", ".")

    #Check if user session exists
    state = check_session()
    if state:
        flash("You are logged in.")
        return redirect(url_for("home"))

    return render_template("sign_in.html", form=form)

@app.route("/sign_in", methods=["POST"])
def post_sign_in():
    #Form Validation
    form = User(request.form)
    username, password = check_login(form, request, True)
    
    #Check if password matches with database password
    user = Users.query.filter_by(username=username).one_or_none()
    if user == None:
        flash("Username/Password doesn't match")
        return redirect(url_for("sign_in"))
    if password == user.password:
        session['name'] = username
        flash("You're Logged in!")
        return redirect(url_for("home"))
    else:
        flash("Username/Password doesn't match")
        return redirect(url_for("sign_in"))

@app.route("/sign_up")
def sign_up():
    form = User()
    
    #Check if user session exists
    state = check_session()
    if state:
        flash("You are logged in.")
        return redirect(url_for("home"))
    return render_template("sign_up.html", range=range, form=form)

@app.route("/sign_up", methods=["POST"])
def post_sign_up():
    form = User(request.form)
    username, password = check_login(form, request)
    new_user = Users(
        username = username,
        password = password,
    )
    try:
        new_user.add()
        new_user.commit()
        flash("You have been registered. Please sign in here.")
    except Exception as e:
        new_user.rollback()
        flash("An error occured!")
        return redirect(url_for("sign_up"))
    return redirect(url_for("sign_in"))

#Handler for the root page
@app.route("/")
def root():
    return render_template("index.html")

#Handler for the home page
@app.route("/home")
def home():
    #Check if user session exists
    state = check_session()
    if not state:
        flash("You are not logged in.")
        return redirect(url_for("sign_in"))

    return render_template("profile.html")

@app.route("/sign_out")
def sign_out():
    #Check if user session exists
    state = check_session()
    if not state:
        flash("You are not logged in.")
        return redirect(url_for("sign_in"))

    #Detach session
    session["name"] = None
    flash("You've been logged out.")
    return redirect(url_for("root"))

@app.route("/suggested_books")
def sign_out():
    #Check if user session exists
    state = check_session()
    if not state:
        flash("You are not logged in.")
        return redirect(url_for("sign_in"))

    return render_template("suggested_books.html")

@app.route("/my_books")
def sign_out():
    #Check if user session exists
    state = check_session()
    if not state:
        flash("You are not logged in.")
        return redirect(url_for("sign_in"))

    return render_template("my_books.html")

"""
#Handler for the profile page
@app.route()
def route():
    pass

#Handler"""