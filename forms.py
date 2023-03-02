from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms import EmailField

from wtforms import validators

class UserForm(Form):
    id = IntegerField('id', [validators.number_range(min = 1, max = 20, message = 'Valor no valido')])
    nombre = StringField('nombre', [
        validators.data_required( message = 'Valor no valido')
    ])
    apaterno = StringField('apaterno', [
        validators.data_required( message = 'Valor no valido')
    ])
    amaterno = StringField('apaterno', [
        validators.data_required( message = 'Valor no valido')
    ])
    email = EmailField('correo', [
        validators.data_required( message = 'Valor no valido'),
        validators.Email( message = 'Ingresa un correo electrónico'
        )
    ])
    