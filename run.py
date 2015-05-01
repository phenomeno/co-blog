#!flask/bin/python
from flask.ext.script import Manager
from app import app, db, models

manager = Manager(app)

@manager.command
def create_all():
    db.create_all()

@manager.command
def create_user(nickname, email, password):
    with app.app_context():
        u = models.User()
        u.nickname = nickname
        u.password = password
        u.email = email
        db.session.add(u)
        db.session.commit()

if __name__ == '__main__':
    manager.run()
