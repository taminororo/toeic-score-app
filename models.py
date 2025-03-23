from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

     # 明示的なリレーション（User → TestScore）
    test_scores = db.relationship('TestScore', back_populates='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# テーブル（モデル）の定義
class TestScore(db.Model):
    __tablename__ = 'TestScore'
    id = db.Column(db.Integer, primary_key=True)  # 主キー
    test_name = db.Column(db.String(80), nullable=True)  # テスト名
    date = db.Column(db.Date, nullable=True)  # 試験日
    
    part_one = db.Column(db.Integer, nullable=True)  # PART1の正解数
    part_two = db.Column(db.Integer, nullable=True)  # PART2の正解数
    part_three = db.Column(db.Integer, nullable=True)  # PART3の正解数
    part_four = db.Column(db.Integer, nullable=True)  # PART4の正解数
    listening = db.Column(db.Integer, nullable=True)  # リスニング全体の正解数

    part_five = db.Column(db.Integer, nullable=True)  # PART5の正解数
    part_six = db.Column(db.Integer, nullable=True)  # PART6の正解数
    part_seven = db.Column(db.Integer, nullable=True)  # PART7の正解数
    reading = db.Column(db.Integer, nullable=True)  # リーディング全体の正解数

    accuracy = db.Column(db.Float, nullable=True)  # 全体の正解数

    #明示的なリレーション（TestScore → User）
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('User', back_populates='test_scores')