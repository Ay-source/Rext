from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()
db = SQLAlchemy()
username=os.getenv("dbusername")
print(username)
password=os.getenv("dbpassword")
host=os.getenv("host")
database_name=os.getenv("database_name")
database_path = f"postgresql://{username}:{password}@{host}/{database_name}"

def setup(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    print(database_path)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app=app
    db.init_app(app)
    Migrate(app, db)

class Books():
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

class User():
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)