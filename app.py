from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
from database.models import setup, User as Users
from auth import check_login, valsave_credentials
from forms import User, Books, username_valid

app = Flask(__name__)
setup(app)
Session(app)

#Route handler for the sign in page
@app.route("/sign_in")
def sign_in():
    form = User()
    try:
        if request.args.get("username", "") in session['name']:
            flash("You're logged in")
            return redirect(url_for("home"))
    except:
        pass
    return render_template("sign_in.html", form=form)

@app.route("/sign_in", methods=["POST"])
def post_sign_in():
    form = User(request.form)
    username, password, permission = check_login(form, request, True)
    user = Users.query.filter_by(username=username).first()
    if password == user.password:
        session['name'] = username
        flash("You're Logged in!")
        return redirect(url_for("home"))
    return redirect(url_for("sign_in"))

@app.route("/sign_up")
def sign_up():
    form = User()
    try:
        if request.args.get("username", "") in session['name']:
            flash("You're logged in")
            return redirect(url_for("home"))
    except:
        pass
    return render_template("sign_up.html", range=range, permissions=["sell:books", "read:books"], form=form)

@app.route("/sign_up", methods=["POST"])
def post_sign_up():
    form = User(request.form)
    username, password, permission = check_login(form, request)
    new_user = Users(
        username = username,
        password = password,
        permission = permission
    )
    try:
        new_user.add()
        new_user.commit()
        flash("You have been registered. Please sign in here.")
    except Exception as e:
        new_user.rollback()
        flash("An error occured!")
        print(e)
        return redirect(url_for("sign_up"))
    return redirect(url_for("sign_in"))

#Handler for the root page
@app.route("/")
def root():
    return render_template("index.html")

#Handler for the home page
@app.route("/home")
def home():
    try:
        if request.args.get("username", "") in session['name']:
            flash("You're logged in")
            return redirect(url_for("home"))
    except:
        flash("You're not logged in")
        return redirect(url_for("root"))
    return render_template("profile.html")

@app.route("/sign_out")
def sign_out():
    try:
        if request.form.get("username", "") not in session['name']:
            flash("please log in")
            return redirect(url_for("sign_in"))
    except:
        flash("You're not logged in")
        return redirect(url_for("home"))
    session["name"] = None
    flash("You've been logged out.")
    return redirect(url_for("sign_in"))

"""
#Handler for the profile page
@app.route()
def route():
    pass

#Handler"""