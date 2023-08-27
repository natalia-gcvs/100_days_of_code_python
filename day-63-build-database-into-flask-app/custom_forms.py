# to create a form using a class that inherit from the flask_wtf.FlaskForm
from flask_wtf import FlaskForm

# to specify what can be inputted into the form fields
from wtforms import StringField, SelectField, SubmitField

# to add validation to our form
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField('Book Name', validators=[DataRequired()])
    author = StringField('Book Author', validators=[DataRequired()])
    rating = SelectField('Rating', choices=[1, 2, 3, 4, 5])
    submit = SubmitField('Submit')

class RatingUpdate(FlaskForm):
    rating = SelectField('Rating', choices=[1, 2, 3, 4, 5])
    submit = SubmitField('Submit')