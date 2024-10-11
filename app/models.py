from app import db
from flask_login import UserMixin
from app import login_manager
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(1000), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    clicks = db.Column(db.Integer, default=0)
    def __repr__(self):
        return f'User {self.username} - clicks: {self.clicks}'


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))
