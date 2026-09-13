from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NotepadForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(),  Length(max=256)])
    body = StringField('Body', validators=[DataRequired()])
    submit = SubmitField('Save notepad')
