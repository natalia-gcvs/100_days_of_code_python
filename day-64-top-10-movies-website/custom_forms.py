from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class UpdateRatingForm(FlaskForm):
    rating = FloatField('Your rating out of 10 e.g. 7.5', validators=[NumberRange(min=1, max=10)])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')
    # year = DateField('Release year e.g. 2021', validators=[Length(min=4, max=4)])
    # description = StringField('Movie overview', validators=[DataRequired(), Length(min=100)])
    # rating = FloatField('Your rating out of 10 e.g. 7.5', validators=[NumberRange(min=1, max=10)])
    # ranking = db.Column(db.Integer, nullable=False)
    # review = db.Column(db.String, nullable=False)
    # img_url = db.Column(db.String, nullable=False)