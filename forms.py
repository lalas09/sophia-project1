from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
class TextForm(FlaskForm):
	text=StringField('Text', validators=[DataRequired()])