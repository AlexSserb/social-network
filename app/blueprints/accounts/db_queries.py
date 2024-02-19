from flask import session

from database import *


def get_user_by_email(email: str) -> User | None:
    return User.query.filter_by(email=email).first()


def get_user_by_username(username: str) -> User | None:
    return User.query.filter_by(username=username).first()


def get_user_by_id(id: int) -> User | None:
    return User.query.filter_by(id=id).first()


def get_current_user() -> User | None:
    if not session['user_id']:
        return None
    return get_user_by_id(session['user_id'])


def create_user(username: str, email: str, password: str):
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


def update_user(user: User, username: str | None, email: str | None, image: FileStorage | None):
    if username and user.username != username:
        user_with_new_username = get_user_by_username(username)
        if user_with_new_username:
            raise Exception('This username is already occupied')
        user.username = username
    if email and user.email != email:
        user_with_new_email = get_user_by_email(email)
        if user_with_new_email:
            raise Exception('This email is already occupied')
        user.email = email
    if image:
        user.set_profile_photo(image)
    
    db.session.add(user)
    db.session.commit()


def delete_profile_photo_user(user: User) -> User:
    user.delete_profile_photo()
    db.session.add(user)
    db.session.commit()
    

def set_following(second_user_id: int, is_follow: bool) -> User:
    user = get_current_user()
    second_user = get_user_by_id(second_user_id)
    if not user or not second_user:
        abort(404)

    if is_follow:
        user.follow(second_user)
    else:
        user.unfollow(second_user)
    return second_user
