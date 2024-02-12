from flask import Blueprint, redirect, render_template, session, url_for, request, flash

from database import db
from .forms import *
from .db_queries import *

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            create_user(form.username.data, form.email.data, form.password.data)
            flash('You registered successfully', 'info')
            return redirect(url_for('auth.login'))
        except Exception as ex:
            flash(str(ex), 'error')
            return redirect(url_for('auth.register'))

    return render_template('auth/register.html', form=form)


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
            redirect(url_for('auth.login'))
    
    return render_template('auth/login.html', form=form)


@bp.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id')
    return redirect(url_for('auth.login'))

