from ext import app

if __name__ == "__main__":
    from routes import home, posts, post_detail, submit_post, about, contact, login, signup, delete_post

    app.run(debug=True)
