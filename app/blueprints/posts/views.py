from flask import Blueprint, redirect, render_template, session, url_for, request, flash
import os

from database import db
from .forms import *
from .db_queries import *

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
