from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired


class UpdateProfileform(FlaskForm):
    first_name = StringField("First name")
    last_name = StringField("Last Name")
    bio = TextAreaField("Bio")
    email = StringField("Email")
    submit = SubmitField("Update")

class Blog_form(FlaskForm):
    title = StringField("Title:", validators=[DataRequired()])
    blog = TextAreaField("Type here:", validators=[DataRequired()])
    submit = SubmitField("Post")

class UpdateBlog_form(FlaskForm):
    title = StringField("Title:", validators=[DataRequired()])
    blog = TextAreaField("Type here:", validators=[DataRequired()])
    submit = SubmitField("Update")
class Comment_form(FlaskForm):
    comment = TextAreaField("Leave a Comment", validators=[DataRequired()])
    comment_by = StringField("Name")
    submit = SubmitField("Comment")
