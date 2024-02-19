from functools import wraps
from flask import redirect, session, url_for


def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('accounts.login'))
        return view(*args, **kwargs)
    return wrapper
