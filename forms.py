from datetime import datetime
from tokenize import Number
from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField, IntegerField
from wtforms.validators import DataRequired, AnyOf, URL

class SalesForm(Form):
    staff_id = IntegerField(
        'staff_id'
    )
    date_time = DateTimeField(
        'date_time',
        validators=[DataRequired()],
        default= datetime.today()
    )
    bread_type = SelectField(
        'type', validators=[DataRequired()],
        choices=[
            ('loaf', 'loaf'),
            ('sliced', 'sliced')
        ]
    )
    bread_size = SelectField(
        'size', validators=[DataRequired()],
        choices=[
            ('20 inch', '20 inch'),
            ('15 inch', '15 inch'),
            ('10 inch', '10 inch'),
            ('7 inch', '7 inch')
        ]
    )
    quantity = IntegerField(
        'quantity', validators=[DataRequired()]
    )
    

class Recipe(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    ingredients = SelectMultipleField(
        'ingredients', validators=[DataRequired()],
        choices=[
            ('Flour', 'Flour'),
            ('Sugar', 'Sugar'),
            ('Salt', 'Salt'),
            ('Yeast', 'Yeast'),
            ('Butter', 'Butter'),
            ('Milk', 'Milk'),
            ('Flavour', 'Flavour'),
            ('Oil', 'Oil'),
            ('Special', 'Special')
        ]
    )

class BreadForm(Form):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    bread_type = SelectField(
        'type', validators=[DataRequired()],
        choices=[
            ('loaf', 'loaf'),
            ('sliced', 'sliced')
        ]
    )
    bread_size = SelectField(
        'size', validators=[DataRequired()],
        choices=[
            ('20 inch', '20 inch'),
            ('15 inch', '15 inch'),
            ('10 inch', '10 inch'),
            ('7 inch', '7 inch')
        ]
    )
    quantity = IntegerField(
        'quantity', validators=[DataRequired()]
    )
