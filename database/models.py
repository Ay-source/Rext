from enum import unique
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ARRAY
from flask_migrate import Migrate
import os

db = SQLAlchemy()


def setup(app):
    app.config.from_object("config")
    db.app=app
    db.init_app(app)
    Migrate(app, db)

class Books(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    author = Column(String, nullable=False, unique=True)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    permission = Column(ARRAY(String), nullable=False)

    def add(self):
        db.session.add(self)

    def commit(self):
        db.session.commit()

    def rollback(self):
        db.session.rollback()