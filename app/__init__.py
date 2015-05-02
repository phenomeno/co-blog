from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.misaka import Misaka


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)
misaka = Misaka(app)

app.secret_key = '/xcbq^/x0c$/x9f/xd9/xe72/xb33uX/xfb/xd3x/x0f/xf3aH/xf9e/x06e'

from app import views
from app import models
