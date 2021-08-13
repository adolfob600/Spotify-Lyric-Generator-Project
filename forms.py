from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextField, PasswordField
from wtforms.validators import DataRequired, Optional

class RegistrationForm(FlaskForm):
    playlistLink = StringField('Enter the link to your Spotify playlist to get started!', validators=[
        DataRequired()])
    submit = SubmitField('Submit')
    
class submitButton(FlaskForm):
    submit = SubmitField('Get Started', validators=[DataRequired(), Optional()])
    