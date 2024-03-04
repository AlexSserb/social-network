from flask import Blueprint, redirect, render_template, session, url_for, request, flash, jsonify
import os

from app.database import db
from .forms import *
from .db_queries import *
from app.blueprints.accounts.utils import *
from app.blueprints.accounts.db_queries import *

bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('/create_post', methods=['GET', 'POST'])
def create_post_view():
    form = CreatePostForm()
    if form.validate_on_submit():
        try:
            create_post(form.title.data, form.content.data, form.image.data)
            flash('Post created successfully', 'info')
            return redirect(url_for('index'))
        except Exception as ex:
            flash(str(ex), 'error')
            return redirect(url_for('posts.create_post_view'))

    return render_template('posts/create_post.html', form=form)


@bp.route('/like/<int:post_id>', methods=['POST'])
@login_required
def like(post_id: int):
    user = get_current_user()

    number_of_likes = like_post(user, post_id)

    return jsonify({ 'likes': number_of_likes })


@bp.route('/delete_like/<int:post_id>', methods=['POST'])
@login_required
def delete_like(post_id: int):
    user = get_current_user()

    number_of_likes = delete_like_post(user, post_id)

    return jsonify({ 'likes': number_of_likes })


@bp.route('/followed_posts', methods=['GET'])
@bp.route('/followed_posts/<int:page>', methods=['GET'])
@login_required
def followed_posts(page: int = 1):
    try:
        user = get_current_user()
        posts = user.get_followed_posts(page)
    except Exception as ex:
        print(ex)
        return redirect(url_for('accounts.login'))

    return render_template('posts/followed_posts.html', current_user=user, posts=posts)
