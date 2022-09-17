import os
import bcrypt
import re
from dotenv import load_dotenv

load_dotenv()

def check_login(form, request, jump=False):
    """Validates the login username and data"""
    """username = request.form.get("username_email")

    #regular expression to validate the username
    userval = re.compile("\W+|_")
    match = re.search(username)"""

    if jump:
        if not form.validate(True):
            return False, False, False

    if not jump:
        if not form.validate():
            return False, False, False

    password = request.form.get("password")

    #Checking if the passwords match
    if "password2" in request.form:
        if password != request.form.get("password2"):
            return (False, "Passwords do not match")

    #using bcrypt to hash the password
    password = bytes(request.form.get("password"), encoding="utf-8")
    salt = bytes(os.getenv("salt"), encoding="utf-8")
    hashed = bcrypt.hashpw(password, salt)

    return (form.useremail.data, hashed.decode("utf-8"), form.permission.data)

def valsave_credentials():
    pass