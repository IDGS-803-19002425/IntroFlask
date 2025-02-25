from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import *
from wtforms import StringField, PasswordField, SubmitField,IntegerField,SelectField,DecimalField,EmailField
from wtforms import validators

class UserForm(Form):
    matricula= StringField('Matricula',[
        validators.DataRequired("El campo es requerido"),
        
    ])
    edad = IntegerField('Edad',[
        validators.DataRequired("El campo es requerido"),        
    ])
    nombre = StringField('Nombre',[
        validators.DataRequired("El campo es requerido"),
        validators.Length(min=2,max=10,message="El campo debe tener entre 2 y 10 caracteres"),
    ])
    apellidos = StringField('Apellidos', [
        validators.DataRequired("El campo es requerido"),
    ])
    email = EmailField('Correo', [
        validators.DataRequired("Ingrese un correo valido"),        
    ])
    


