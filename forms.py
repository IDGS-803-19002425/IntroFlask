from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import *
from wtforms import StringField, PasswordField, SubmitField,IntegerField,SelectField,DecimalField,EmailField

class UserForm(Form):
    matricula= StringField('Matricula')
    edad = IntegerField('Edad')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    email = EmailField('Email')
