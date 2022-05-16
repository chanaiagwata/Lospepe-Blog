from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Blogs, Comment, Subscribers, Quotes
from flask_login import login_required

#Views
@main.route('/')
def index():
    
    title = "here we are"
    
    return render_template('index.html', title=title)

@main.route('/blog/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    '''
    '''