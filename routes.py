from flask import render_template, redirect
from flask_login import login_user, logout_user, current_user, login_required
from forms import BlogPostForm, SignUpForm, LogInForm, CommentForm
from ext import app, db
from models import Post, User, Comment


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/posts')
def posts():
    posts_list = Post.query.all()
    return render_template('posts.html', posts=posts_list)


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post_detail(post_id):
    post = Post.query.get(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(content=form.content.data, post_id=post_id, user_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(f'/post/{post_id}')
    comments = Comment.query.filter_by(post_id=post_id).all()
    return render_template('post_detail.html', post=post, form=form, comments=comments)


@app.route('/submit_post', methods=['GET', 'POST'])
@login_required
def submit_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, content=form.content.data, excerpt=form.excerpt.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect("/posts")
    return render_template('create_post.html', form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data, email=form.email.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect("/login")
    return render_template('sign_up.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect("/")
    return render_template('log_in.html', form=form)


@app.route('/delete_post/<int:post_id>')
@login_required
def delete_post(post_id):
    if current_user.role == "Admin":
        post = Post.query.get(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return redirect("/posts")


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')
