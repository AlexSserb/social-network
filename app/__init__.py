from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template_string, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap5

from datetime import datetime

from .database import db
from .blueprints.accounts.db_queries import get_current_user
from .blueprints.accounts.utils import login_required
from .blueprints.posts.db_queries import get_all_posts


def create_app(config_name='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_name)

    db.init_app(app)
    migrate = Migrate(app, db)
    bootstrap = Bootstrap5(app)


    def format_datetime(value, format="%Y.%m.%d %H:%M"):
        if value is None:
            return ""
        return value.strftime(format)

    app.jinja_env.filters['date_format']=format_datetime


    from app.blueprints import accounts, posts
    app.register_blueprint(accounts)
    app.register_blueprint(posts)


    @app.route('/', methods=['GET'])
    @app.route('/<int:page>', methods=['GET'])
    @login_required
    def index(page: int = 1):
        try:
            user = get_current_user()
            posts = get_all_posts(page)
        except Exception as ex:
            print(ex)
            return redirect(url_for('accounts.login'))

        return render_template('index.html', current_user=user, posts=posts)

    return app