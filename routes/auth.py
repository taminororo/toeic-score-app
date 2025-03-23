from functools import wraps
from flask import session, Blueprint, redirect, url_for, flash, Flask, render_template, request
from models import db, User
from forms import SignupForm, LoginForm

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data

        if User.query.filter_by(username=username).first():
            flash("すでにそのユーザー名は使われています。")
            return render_template('signup.html', form=form)

        user = User(username=username)
        user.set_password(password)  # パスワードはハッシュ化される前提
        db.session.add(user)
        db.session.commit()

        flash("登録が完了しました。ログインしてください。")
        return redirect(url_for('auth.login'))

    # GETリクエスト または バリデーション失敗
    return render_template('signup.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            session.clear()  # セッション固定攻撃対策
            session['user_id'] = user.id
            session['username'] = user.username
            return redirect(url_for('test.home'))
        else:
            flash("ログイン失敗。ユーザー名またはパスワードが間違っています。")

    return render_template('login.html', form=form)

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))