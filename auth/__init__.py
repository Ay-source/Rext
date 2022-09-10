import os
import bcrypt
from dotenv import load_dotenv

load_dotenv()

def check_login():
    username = request.form.get("username")
    password = bytes(request.form.get("password"), encoding="sutf-8")
    salt = os.getenv("salt")
    hashed = bcrypt.hashpw(password, salt)
