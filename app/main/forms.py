from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField,TextAreaField
from wtforms.validators import ValidationError, DataRequired


class PostForm(FlaskForm):
    post = TextAreaField(('blog something'), validators=[DataRequired()])
    category = SelectField('Category', choices=[('Technology','Technology'),('Sales','Sales')])
    submit = SubmitField(('Submit'))

class CommentForm(FlaskForm):
    details = StringField('Write a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')
