from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.datastructures import FileStorage
from flask import current_app

from uuid import uuid4
from datetime import datetime
import os

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    posts = db.relationship('Post', backref='user')

    def __repr__(self):
        return f'<{self.id}: {self.username}>'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,  password):
	    return check_password_hash(self.password_hash, password)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), nullable=False)
    image = db.Column(db.String(256))
    content = db.Column(db.Text(), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def _repr__(self):
        return f'<Autor: {self.user.id}, title: {self.title}>'

    def set_image(self, image_file: FileStorage):
        filename = image_file.filename
        directory = os.path.join(current_app.root_path, 'static', 'images', 'post_images')
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        new_filename = str(uuid4()) + os.path.splitext(filename)[-1]
        image_path = os.path.join(directory, new_filename)
        image_file.save(image_path)
        self.image = os.path.join('images', 'post_images', new_filename).replace('\\', '/')
