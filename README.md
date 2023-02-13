# Rext
## Introduction
Rext is an online bookstore and also functions as a chat app.

## Installation
Prerequisites:
- python3
- postgres

Installation steps:

1. Clone the repo from github [here](https://github.com/Ay-source/Rext.git) or copy the link below

    `https://github.com/Ay-source/Rext.git`
2. Install the requirements. 

    `python -m pip install -r requirements.txt`
3. set the following environment variables in:

    For terminal:

            `export FLASK_APP=app.py`

            `export FLASK_DEBUG=app.py`

    For command line:

            `set FLASK_APP=app.py`
    
            `set FLASK_DEBUG=app.py`

4. Run python in the terminal/command line general and generate hash for step 5.
```
$ python
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import bcrypt
>>> bcrypt.gensalt()
b'$2b$12$Nrk2pgnWfbqIdHCK4GqRRO'
>>>
```

5. Create a file called .env in the root of the cloned repo. It should contain:
```
    dbusername=postgres
    dbpassword=postgres
    database_name=Rext
    host=127.0.0.1:5432
    salt=$2b$14$FrDHPdVQzD3wdn0kx0vDLu
```
6. Ensure postgres server is running and that database exists.

7. If running the app for the first time, run the following in your command line/terminal
```
flask db init
flask db migrate
flask db upgrade
```

4. type `flask run` into the terminal/commandline

## Structure
"""

Rext

    app.py
    |
    database
        |
        __init__.py
    |
    auth
        |
        __init__.py
    |
    forms
        |
        __init__.py

"""
