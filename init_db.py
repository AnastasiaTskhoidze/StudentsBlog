from ext import app, db
from models import Post, User, Comment

with app.app_context():
    db.create_all()

    admin_user = User("ADMIN", "ADMINpassword", "studentsblog@gmail.com", "Admin")
    db.session.add(admin_user)
    db.session.commit()
