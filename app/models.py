from . import db, login_manager
# from . import *
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from time import time
import jwt
from app import create_app
# from app import *

class Article(db.Model):
    '''
    definition of author objects
    '''
    __tablename__= 'article'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    category = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.relationship('Comment', backref='article', lazy="dynamic")
    @classmethod
    def retrieve_posts(cls,id):
        article = Article.filter_by(id=id).all()
        return article
# user


    '''
    this class represent all articles by users.
    The user_id field is initialized as a foreign key to user.id,
    which means that it references an id value from the users table
    '''
    # tablenametabletablenamenatablenametablenamemedef __init__(self , id, Article, author, comment, url, urlToImage, publishedAt):
    #     self.id = id
    #     self.Article = Article
    #     self.author = author
    #     self.comment = comment
    #     self.url = url
    #     self.urlToImge = urlToImage
    #     self.publishedAt = publishedAt    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'))



class User(UserMixin, db.Model):
    '''
    UserMixin class that helped with implementations appropriate foruser model class
    '''
    __tablename__ = 'user'
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique = True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(130))
    Article = db.relationship('Article', backref='author', lazy='dynamic')
    bio = db.Column(db.String(255))
    profile_pic = db.Column(db.String(255))
    Article = db.relationship('Article',backref = 'user',lazy = "dynamic")
    comment = db.relationship('Comment', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('cannot read password attribute')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        '''
        these methods allowsecure password verification
        '''
    def __repr__(self):
        return '{}'.format(self.body)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    def save_user(self):
        db.session.add(self)
        db.session.commit()

class Comment(db.Model):
    __tablename__='comment'
    id = db.Column(db.Integer,primary_key= True)
    details = db.Column(db.String(255))
    article_id = db.Column(db.Integer,db.ForeignKey('article.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
