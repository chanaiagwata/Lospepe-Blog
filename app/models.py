from . import db
from datetime import datetime
from . import db



#users
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True, index=True)
    comment = db.relationship("Comments", backref = "user", lazy = "dynamic")

    def __ref__(self):
        return f'User{self.username}'
#writer
class Writer(db.Model):
    __tablename__ = 'writer'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    blog_id = db.Column(db.Integer, db.ForeignKey("blogs.id"))

#Blogs
class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    blog = db.Column(db.String(255))
    writer = db.relationship("Writer", backref  = "writer", lazy = "dyamic")
    
    
#Comments
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    opinion = db.Column(db.String(255))
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
#Comments
class Quotes:
    '''
    Quotes class to define random quote objects
    '''
    
    def __init__(self,id):
        self.id = id