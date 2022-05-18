from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#users
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique=True, index=True)
    bio = db.Column(db.String())
    pass_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    comment = db.relationship("Comment", backref = "user", lazy = "dynamic")
    blogs = db.relationship("Blogs", backref = "user", lazy = "dynamic" )

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.pass_secure  = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
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
    
    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_blogs(cls):
        return Blogs.query.order_by(Blogs.posted_at).all()
#Comments
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    opinion = db.Column(db.String)
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    opinion_by = db.Column(db.String(255))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer,db.ForeignKey('blogs.id'))
    
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def delete_comment(cls,id):
        del_comment = Comment.query.filter_by(id=id).first()
        db.session.delete(del_comment)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,id):
        comment = Comment.query.filter_by(blog_id = id).all()
        return comment

    
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