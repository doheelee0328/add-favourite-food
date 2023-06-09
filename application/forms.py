from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class UserDataForm(FlaskForm):
  item = StringField("Item", validators =[DataRequired()])
  votes = IntegerField("Votes", validators=[DataRequired(), NumberRange(min=1, max=10)])
  submit = SubmitField("Generate Item")

class UpdateUserDataForm(FlaskForm):
  item = StringField("Item", validators =[DataRequired()])
  votes = IntegerField("Votes", validators=[DataRequired(), NumberRange(min=1, max=10)])
  submit = SubmitField("Save")