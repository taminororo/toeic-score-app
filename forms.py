# forms.py

from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.validators import DataRequired, NumberRange
from wtforms import StringField, IntegerField, SubmitField, DateField, PasswordField
from wtforms.validators import DataRequired, Length

class TestForm(FlaskForm):
    test_name = StringField('テスト名', validators=[DataRequired()])
    date = DateField('日付', validators=[DataRequired()])
    part_one = IntegerField('PART1 正答数', validators=[DataRequired(), NumberRange(min=0, max=6)])
    part_two = IntegerField('PART2 正答数', validators=[DataRequired(), NumberRange(min=0, max=25)])
    part_three = IntegerField('PART3 正答数', validators=[DataRequired(), NumberRange(min=0, max=39)])
    part_four = IntegerField('PART4 正答数', validators=[DataRequired(), NumberRange(min=0, max=30)])
    part_five = IntegerField('PART5 正答数', validators=[DataRequired(), NumberRange(min=0, max=30)])
    part_six = IntegerField('PART6 正答数', validators=[DataRequired(), NumberRange(min=0, max=16)])
    part_seven = IntegerField('PART7 正答数', validators=[DataRequired(), NumberRange(min=0, max=54)])
    submit = SubmitField('保存する')


class DeleteForm(FlaskForm):
    submit = SubmitField("削除")

class SignupForm(FlaskForm):
    username = StringField('ユーザー名', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('パスワード', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('登録')

class LoginForm(FlaskForm):
    username = StringField('ユーザー名', validators=[DataRequired()])
    password = PasswordField('パスワード', validators=[DataRequired()])
    submit = SubmitField('ログイン')
