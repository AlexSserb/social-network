from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, render_template_string, render_template, request, session, redirect, url_for
from flask_bootstrap import Bootstrap5

import redis

from database import db
from blueprints.auth.db_queries import get_current_user

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)


from blueprints import *
app.register_blueprint(auth)


@app.route('/')
def index():
    try:
        user_id = session['user_id']
        user = get_current_user()
    except:
        return redirect(url_for('auth.login'))
    
    return render_template('index.html', username=user.username)


if __name__ == '__main__':
    app.run()
