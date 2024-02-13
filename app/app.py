from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template_string, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap5

from datetime import datetime

from database import db
from blueprints.auth.db_queries import get_current_user
from blueprints.posts.db_queries import get_all_posts


app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)


def format_datetime(value, format="%d-%m-%Y"):
    if value is None:
        return ""
    return value.strftime(format)

app.jinja_env.filters['date_format']=format_datetime


from blueprints import *
app.register_blueprint(auth)
app.register_blueprint(posts)


@app.route('/')
def index():
    try:
        user_id = session['user_id']
        user = get_current_user()
        posts = get_all_posts()
    except:
        return redirect(url_for('auth.login'))

    print(app.config['UPLOAD_FOLDER'])
    
    return render_template('index.html', username=user.username, posts=posts)


if __name__ == '__main__':
    app.run()
