from flask_wtf import FlaskForm
from wtforms import StringField , SubmitField ,TextAreaField

class MyForm(FlaskForm):
  name = StringField('Name')
  submit = SubmitField('Submit')


class ContactForm(FlaskForm):
  name = StringField('Name')
  email = StringField('Email')
  message = TextAreaField('Message')
  submit = SubmitField('Submit')