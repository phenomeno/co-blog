#!flask/bin/python
from flask.ext.script import Manager, Server
from app import app, db, models
import os

app.debug=True

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

manager.add_command('runserver', Server(host='0.0.0.0', port=os.environ.get('PORT', 5000)))

if __name__ == '__main__':
    manager.run()
