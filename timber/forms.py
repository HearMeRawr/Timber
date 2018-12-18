from wtforms import *

class Register(Form):
  email = StringField("Email", [validators.Length(min=5, max=256)])
  password = PasswordField("Password", [validators.DataRequired(), validators.EqualTo("passwordConfirm", message="Passwords must match")])
  passwordConfirm = PasswordField("Confirm password", [validators.DataRequired()])

class Login(Form):
  email = StringField("Email", [validators.Length(min=5, max=256)])
  password = PasswordField("Password", [validators.DataRequired()])