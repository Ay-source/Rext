import os
from dotenv import load_dotenv

load_dotenv()

#Initiate secret key
SECRET_KEY=os.urandom(32)

#Load variables from .env file
username=os.getenv("dbusername")
password=os.getenv("dbpassword")
host=os.getenv("host")
database_name=os.getenv("database_name")

#initiate database path
database_path = f"postgresql://{username}:{password}@{host}/{database_name}"


SQLALCHEMY_DATABASE_URI = database_path
SQLALCHEMY_TRACK_MODIFICATIONS = False
SESSION_PERMANENT=False
SESSION_TYPE="filesystem"