from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, TelField, EmailField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class Form_add_category(FlaskForm):
    # strf = StringField('Srting', validators=[DataRequired()])
    # boolf = BooleanField('Bool')
    # telf = TelField('Tel')
    # emf = EmailField('Mail')
    textf = TextAreaField('Text')
    submit = SubmitField('Send')

class Form_add_news(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    # boolf = BooleanField('Bool')
    # telf = TelField('Tel')
    # emf = EmailField('Mail')
    textf = TextAreaField('Text')
    category_id = SelectField('category_id',choices=[('1','1'),('2','2'),('3','3')])
    submit = SubmitField('Send')