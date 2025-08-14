from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    in_stock = BooleanField('In Stock')
    description = TextAreaField('Description')
    submit = SubmitField('Save')
