from flask import session
from werkzeug.datastructures import FileStorage

from database import *


def get_all_posts():
    return Post.query.all()
    

def create_post(title: str, content: str, image: FileStorage | None):
    try:
        user_id = session['user_id']
        post = Post(title=title, content=content, user_id=user_id)
        if image:
            post.set_image(image)
        db.session.add(post)
        db.session.commit()
    except Exception as ex:
        raise Exception('You are not authorized to create posts')
    