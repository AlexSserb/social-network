from flask import session

from database import *


def get_user_by_email(email) -> User | None:
    return User.query.filter_by(email=email).first()


def get_user_by_username(username) -> User | None:
    return User.query.filter_by(username=username).first()


def get_current_user() -> User | None:
    if not session['user_id']:
        return None
    return User.query.filter_by(id=session['user_id']).first()


def create_user(username, email, password):
    user = get_user_by_email(email)
    if user:
        raise Exception('This email is already occupied')

    user = get_user_by_username(username)
    if user:
        raise Exception('This username is already occupied')
    
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

