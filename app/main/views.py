from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Blogs, Comment, Subscribers, Quotes


#Views
@main.route('/')
def index():
    
    title = "here we are"
    
    return render_template('index.html', title=title)