from ext import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    excerpt = db.Column(db.String())


class Comment(db.Model):
    __tablename__ = "comments"

    id = db.Column(db.Integer(), primary_key=True)
    content = db.Column(db.String())
    post_id = db.Column(db.Integer(), db.ForeignKey("posts.id"))
    user_id = db.Column(db.Integer(), db.ForeignKey("users.id"))
    user = db.relationship("User")

    def __init__(self, content, post_id, user_id):
        self.content = content
        self.post_id = post_id
        self.user_id = user_id


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())
    email = db.Column(db.String())
    role = db.Column(db.String())

    def __init__(self, username, password, email, role="Guest"):
        self.username = username
        self.password = generate_password_hash(password)
        self.email = email
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
