from flask import Flask, render_template, request, redirect, url_for, flash
from database.models import setup, User as Users
from auth import check_login, valsave_credentials
from forms import User, Books, username_valid

app = Flask(__name__)
setup(app)


#Route handler for the sign in page
@app.route("/sign_in")
def sign_in():
    form = User()
    return render_template("sign_in.html", form=form)

@app.route("/sign_in", methods=["POST"])
def post_sign_in():
    form = User()
    username, password, permission = check_login(form, request)
    user = Users.query.filter_by(username=username)
    if password == user.password:
        flash("You're Logged in!")
        return redirect(url_for("root"))
    return redirect(url_for("sign_in"))

@app.route("/sign_up")
def sign_up():
    form = User()
    return render_template("sign_up.html", range=range, permissions=["sell:books", "read:books"], form=form)

@app.route("/sign_up", methods=["POST"])
def post_sign_up():
    form = User()
    username, password, permission = check_login(form, request)
    new_user = Users(
        username = username,
        password = password,
        permission = permission
    )
    try:
        new_user.add()
        new_user.commit()
        flash("You're Registered!")
    except Exception as e:
        new_user.rollback()
        flash("An error occured!")
        print(e)
        return redirect(url_for("sign_up"))
    return redirect(url_for("root"))

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