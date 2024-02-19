from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template_string, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap5

from datetime import datetime

from database import db
from blueprints.accounts.db_queries import get_current_user
from blueprints.accounts.utils import login_required
from blueprints.posts.db_queries import get_all_posts


app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)


def format_datetime(value, format="%Y.%m.%d %H:%M"):
    if value is None:
        return ""
    return value.strftime(format)

app.jinja_env.filters['date_format']=format_datetime


from blueprints import *
app.register_blueprint(accounts)
app.register_blueprint(posts)


@app.route('/')
@login_required
def index():
    try:
        user_id = session['user_id']
        user = get_current_user()
        posts = get_all_posts()
    except:
        return redirect(url_for('accounts.login'))

    return render_template('index.html', username=user.username, posts=posts)


if __name__ == '__main__':
    app.run()
