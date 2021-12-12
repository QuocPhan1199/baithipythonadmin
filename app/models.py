from app import db
from app import login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.String(24))
    password = db.Column(db.String(128))
    def __init__(self, username,email, password):
        self.username = username
        self.email = email
        self.set_password(password)
    def set_password(self, password):
        self.password = password
    # def check_password(self, password):
    #     return check_password_hash(self.password, password)
    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def __str__(self):
        return self.username
    def __repr__(self):
        return '<User> {}'.format(self.username, self.password, self.email)
class Tin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.String(255))
    images = db.Column(db.String(255))
    id_Loaitin = db.Column(db.Integer, db.ForeignKey('loai_tin.id'))
    tomtat = db.Column(db.String(255))
    status = db.Column(db.Integer)
    def __init__(self, title,content, images, id_Loaitin, tomtat, status):
        self.title = title
        self.content = content
        self.images = images
        self.id_Loaitin = id_Loaitin
        self.tomtat = tomtat
        self.status = status
    def __repr__(self):
        return '<Tin> {}'.format( self.title, self.content, self.images, self.id_Loaitin, self.tomtat, self.status)

class LoaiTin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tenloai = db.Column(db.String(255))
    def __repr__(self):
        return '<LoaiTin> {}'.format(self.id, self.tenloai)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))