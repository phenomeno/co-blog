from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

app.secret_key = '/xcbq^/x0c$/x9f/xd9/xe72/xb33uX/xfb/xd3x/x0f/xf3aH/xf9e/x06e'

from app import views
from app import models

if len(models.User.query.all()) == 0:
    u = models.User()
    u.username = 'test'
    u.email = 'test@email.com'
    u.password = 'pass'
    db.session.add(u)
    db.session.commit()
