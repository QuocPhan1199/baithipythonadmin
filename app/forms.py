# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, validators, PasswordField,TextField,validators
# from wtforms.validators import DataRequired
# from app.models import User
# from app.models import LoaiTin
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
class LoaiTinForm(FlaskForm):
    tenloai = StringField('Tenloai', validators=[DataRequired()])
    submit = SubmitField('Submit')

class TinForm(FlaskForm):
    loaitin =StringField('Loaitin', validators=[DataRequired()])
    tieude = StringField('Tieude', validators=[DataRequired()])
    tomtat = StringField('Tomtat', validators=[DataRequired()])
    noidung = StringField('Noidung', validators=[DataRequired()])
    images = StringField('Images', validators=[DataRequired()])
    status = StringField('Status', validators=[DataRequired()])
    submit = SubmitField('Submit')   