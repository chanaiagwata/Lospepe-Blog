from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Writer, Blogs, Comment


#Views
@main.route('/')
def index():
    
    title = "here we are"
    
    return render_template('index.html', title=title)