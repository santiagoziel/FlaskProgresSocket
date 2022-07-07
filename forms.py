from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms.validators import InputRequired, Length, ValidationError

class deckUploadForm(FlaskForm):
    file = FileField()
