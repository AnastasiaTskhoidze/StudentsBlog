from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length


class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = TextAreaField('Content', validators=[InputRequired()])
    excerpt = StringField('Excerpt', validators=[InputRequired(), Length(max=150)])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Comment')

class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(), Length(min=6, max=36)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=8, max=64)])
    email = EmailField('Email', validators=[InputRequired()])
    submit = SubmitField('Sign Up')


class LogInForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log in')
