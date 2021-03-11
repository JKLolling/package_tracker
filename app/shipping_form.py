from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, SelectField
from wtforms.validators import DataRequired
from map.map import map

origin_list = [(origin, origin) for origin in map.keys()]


class ShippingForm(FlaskForm):
    sender = StringField('Sender', [DataRequired()])
    recipient = StringField('Recipient', [DataRequired()])
    origin = SelectField('Origin', [DataRequired()], choices=origin_list)
    destination = SelectField(
        'Destination', [DataRequired()], choices=origin_list)
    express = BooleanField('Express Shipping', [DataRequired()])
