from flask import session
from werkzeug.datastructures import FileStorage
from sqlalchemy import desc

from config import POSTS_PER_PAGE
from database import *


def get_all_posts(page: int):
    return Post.query.order_by(desc(Post.created_on)) \
        .paginate(page=page, per_page=POSTS_PER_PAGE, error_out=False)


def get_posts_of_user(user_id: int, page: int):
    return Post.query.filter_by(user_id=user_id).order_by(desc(Post.created_on)) \
        .paginate(page=page, per_page=POSTS_PER_PAGE, error_out=False)
    

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
    

# Create object "Like" for post and user. Returns number of likes for current post.
def like_post(user: User, post_id: int) -> int:
    if not Like.query.filter_by(user_id=user.id, post_id=post_id).first():
        like = Like(user_id=user.id, post_id=post_id)
        db.session.add(like)
        db.session.commit()
    return Like.query.filter_by(post_id=post_id).count()


# Remove object "Like" for post and user. Returns number of likes for current post.
def delete_like_post(user: User, post_id: int) -> int:
    like = Like.query.filter_by(user_id=user.id, post_id=post_id).first()
    if like:
        db.session.delete(like)
        db.session.commit()
    return Like.query.filter_by(post_id=post_id).count()