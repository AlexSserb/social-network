from flask import Blueprint, redirect, render_template, session, url_for, request, flash, abort

from database import db
from .forms import *
from .db_queries import *

bp = Blueprint('accounts', __name__, url_prefix='/accounts')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            create_user(form.username.data, form.email.data, form.password.data)
            flash('You registered successfully', 'info')
            return redirect(url_for('accounts.login'))
        except Exception as ex:
            flash(str(ex), 'error')
            return redirect(url_for('accounts.register'))

    return render_template('accounts/register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_username(form.username.data)
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            return redirect('/')
        else:
            flash('Incorrect username or password', 'error')
            redirect(url_for('accounts.login'))
    
    return render_template('accounts/login.html', form=form)


@bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id')
    return redirect(url_for('accounts.login'))


@bp.route('/profile/<int:user_id>', methods=['GET'])
def profile(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        abort(404)
    return render_template('accounts/profile.html', user=user)
    

@bp.route('/profile_editor/<int:user_id>', methods=['GET', 'POST'])
def profile_editor(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        abort(404)
    form = ProfileEditForm(username=user.username, email=user.email)
    if form.validate_on_submit():
        try:
            update_user(user, form.username.data, form.email.data, form.image.data)
            flash('Profile changed successfully', 'info')
            return redirect(url_for('accounts.profile', user_id=user_id))
        except Exception as ex:
            flash(str(ex), 'error')
            return redirect(url_for('accounts.profile_editor', user_id=user_id))
    
    return render_template('accounts/profile_editor.html', form=form, user=user)


@bp.route('/remove_profile_photo/<int:user_id>', methods=['POST'])
def remove_profile_photo(user_id: int):
    user = get_user_by_id(user_id)
    if not user:
        abort(404)
    delete_profile_photo_user(user)
    flash('Profile photo deleted successfully', 'info')
    return redirect(url_for('accounts.profile_editor', user_id=user_id))
