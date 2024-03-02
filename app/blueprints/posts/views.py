from flask import Blueprint, redirect, render_template, session, url_for, request, flash, jsonify
import os

from database import db
from .forms import *
from .db_queries import *
from blueprints.accounts.utils import *
from blueprints.accounts.db_queries import *

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
