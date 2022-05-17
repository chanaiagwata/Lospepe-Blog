from flask import render_template,request,redirect,url_for
from . import main
from ..models import User, Blogs, Comment, Subscribers, Quotes
from .forms import Blog_form, Comment_form, UpdateBlog_form, UpdateProfileform
from flask_login import login_required, current_user


from datetime import datetime
from ..email import mail_message
from .. import db
from ..requests import get_quote

#Views
@main.route("/", methods = ["GET","POST"])
def index():
    blog = Blogs.get_blog()
    quote = get_quote()
     
    if request.method =="POST":
        new_subscriber = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_subscriber)
        db.session.commit()
        
        mail_message("Welcome to ChanaiBlogs", new_subscriber.email)
    
    return render_template("index.html", blogs = blog, quote = quote)


@main.route('/blog/<int:id>', methods = ['GET','POST'])
def blog(id):
    blog = Blogs.query.filter_by(id = id).first()
    comments = Comment.query.filter_by(blog_id = id).all()
    commentsForm = Comment_form()
    
    
    if commentsForm.validate_on_submit():
        comment = commentsForm.comment_by.data
        commentsForm.comment.data = ""
        commentedby = commentsForm.comment_by.data
        commentsForm.comment_by.data=""
        if current_user.is_authenticated:
            commentedby = current_user.username
        new_comment = Comment(comment = comment, commented_by =commentedby, comment_at=datetime.now(), post_id=id,)
        new_comment.save_comment()
        return redirect(url_for("main.blog", id = blog.id))
    return render_template("blog.html", blog = blog, comments = comments, commentform = commentsForm)

@main.route("/blog/<int:id>/update", methods = ["POST", "GET"])
@login_required
def edit_blog(id):
    blog = Blogs.query.filter_by(id=id).first()
    edit_form = UpdateBlog_form
    
    if edit_form.validate_on_submit():
        blog.blog_title = edit_form.title.data
        edit_form.title.data=""
        blog.blog_content = edit_form.blog.data
        edit_form.blog.data ="" 
        
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for("main.blog", id = blog.id))
    return render_template("edit_blog.html, blog=blog, edit_form=edit_form")

@main.route("/blog/<int:id>/<int:comment_id>/delete")
def delete_comment(id, comment_id):
    blog = Blogs.query.filter_by(id = id).first()
    comment = Comment.query.filter_by(id = comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for("main.blog", id = blog.id))


@main.route("/profile/<int:id>/<int:blog_id>/delete")
@login_required
def delete_post(id, blog_id):
    user = User.query.filter_by(id = id).first()
    blog = Blogs.query.filter_by(id = blog_id).first()
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for("main.profile", id = user.id))

@main.route("/profile/<int:id>", methods = ["POST", "GET"])
def profile(id):
    user = User.query.filter_by(id = id).first()
    posts = Blogs.query.filter_by(user_id = id).all()

    if request.method == "POST":
        new_sub = Subscribers(email = request.form.get("subscriber"))
        db.session.add(new_sub)
        db.session.commit()
        mail_message("Thank you for subscribing to ChanaiBlogs, welcome")

    return render_template("profile/profile.html",
                            user = user,
                            posts = posts)
    
@main.route("/blog/new", methods = ["POST", "GET"])
@login_required
def new_blog():
    blog_form = Blog_form()
    if blog_form.validate_on_submit():
        blog_title = blog_form.title.data
        blog_form.title.data = ""
        
        blog_form.blog.data=""
        new_blog = Blogs(blog_title = blog_title, posted_at = datetime.now(), post_by = current_user.username, user_id = current_user.id)
        new_blog.save_blog()
        subscribers = Subscribers.query.all()
        for subscriber in subscribers:
            mail_message(blog_title, subscriber.email, new_post = new_blog)
            pass
        return redirect(url_for("main.blog", id = new_blog.id))
    return render_template("new_blog.html", blog_form = blog_form)