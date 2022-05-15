from . import db
from datetime import datetime
from . import db



#users
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True, index=True)
    comment = db.relationship("Comments", backref = "user", lazy = "dynamic")
    blogs = db.relationship("Blogs", backref = "user", lazy = "dynamic" )

    def __ref__(self):
        return f'User{self.username}'
#Blogs
class Blogs(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    blog_title = db.Column(db.String)
    blog_content = db.Column(db.Text)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    written_by = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comments = db.relationship("Comment", backref = "blog", lazy = "dynamic")
    
#Comments
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    opinion = db.Column(db.String)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    opinion_by = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    
#Comments
class Quotes:
    '''
    Quotes class to define random quote objects from API
    '''
    
    def __init__(self,author,quote):
        self.author = author
        self.quote = quote

#subscriber
class Subscribers(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)