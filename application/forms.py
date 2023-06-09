from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, IntegerField
from wtforms.validators import DataRequired

class UserDataForm(FlaskForm):
  item = StringField("Item", validators =[DataRequired()])
  votes = IntegerField("Votes", validators=[DataRequired()])
  submit = SubmitField("Generate Item")

class UpdateUserDataForm(FlaskForm):
  item = StringField("Item", validators =[DataRequired()])
  votes = IntegerField("Votes", validators=[DataRequired()])
  submit = SubmitField("Update Item")