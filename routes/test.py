# routes/test.py
from flask import Blueprint
from models import User, db, TestScore
from flask import Flask, render_template, request, session
from datetime import datetime
from utils import login_required
from forms import TestForm, DeleteForm
test_bp = Blueprint('test', __name__)



@test_bp.route('/')
def home():
    message = "TOEICの模試のスコアを記録しよう"

    return render_template('home.html', message = message)

@test_bp.route('/test_list')
@login_required
def test_list():
    message = "過去の記録"

    # ログインユーザーのIDを取得
    user_id = session['user_id']
    tests = TestScore.query.filter_by(user_id=user_id).all()  # テストの一覧を取得
    delete_form = DeleteForm()  # 削除用のフォームを生成
    return render_template('test_list.html', tests = tests, message = message, delete_form=delete_form)

@test_bp.route('/new')
@login_required
def new():
    message = "入力ページ"
    form = TestForm()  # ✅ CSRFトークンを含んだフォームインスタンスを生成

    return render_template('new.html', message=message, form=form)

@test_bp.route('/create', methods=['POST'])
@login_required
def create():
    print("フォーム内容:", request.form)
    print("✅ create() に入った")
    
    form = TestForm()
    
    if form.validate_on_submit():
        new_test = TestScore()

        new_test.user_id = session['user_id']  # ログイン中のユーザーID

        # フォームの値を取得（FlaskFormを使えばdata属性にアクセスするだけ！）
        new_test.test_name = form.test_name.data
        new_test.date = form.date.data
        new_test.part_one = form.part_one.data
        new_test.part_two = form.part_two.data
        new_test.part_three = form.part_three.data
        new_test.part_four = form.part_four.data
        new_test.part_five = form.part_five.data
        new_test.part_six = form.part_six.data
        new_test.part_seven = form.part_seven.data

        print("✅ 各パートの値を取得完了")

        new_test.listening = (
            new_test.part_one + new_test.part_two + new_test.part_three + new_test.part_four
        )
        new_test.reading = (
            new_test.part_five + new_test.part_six + new_test.part_seven
        )
        new_test.accuracy = new_test.listening + new_test.reading

        db.session.add(new_test)
        db.session.commit()

        print("✅ DBに保存成功")

        test = TestScore.query.get(new_test.id)
        message = "本当にこの内容で保存しますか？"
        return render_template('create.html', test=test, message=message)

    else:
        print("❌ バリデーション失敗:", form.errors)
        # 失敗したらnew.htmlに戻す（エラー表示も可能）
        return render_template('new.html', form=form, message="入力内容に不備があります")

    
@test_bp.route('/destroy/<int:id>', methods=['GET', 'POST'])
@login_required
def destroy(id):
    form = DeleteForm()

    if request.method == 'POST':
        if not form.validate_on_submit():
            # CSRFトークンが無効 or 改ざんされたリクエスト
            message = '不正なリクエストです（CSRFトークンエラー）'
            user_id = session['user_id']
            tests = TestScore.query.filter_by(user_id=user_id).all()
            return render_template('test_list.html', message=message, tests=tests, delete_form=DeleteForm())

        from_page = request.form.get('from_')
    else:
        from_page = request.args.get('from_')

    print(from_page)

    if from_page == 'CREATE':
        message = '登録をキャンセルしました'
    elif from_page == 'DELETE':
        message = 'データを削除しました'
    else:
        message = 'その方法では削除できません'
        user_id = session['user_id']
        tests = TestScore.query.filter_by(user_id=user_id).all()
        return render_template('test_list.html', message=message, tests=tests, delete_form=DeleteForm())

    destroy_post = TestScore.query.get(id)

    if destroy_post is None:
        message = '指定されたデータは存在しません'
        user_id = session['user_id']
        tests = TestScore.query.filter_by(user_id=user_id).all()
        return render_template('test_list.html', message=message, tests=tests, delete_form=DeleteForm())

    db.session.delete(destroy_post)
    db.session.commit()

    user_id = session['user_id']
    tests = TestScore.query.filter_by(user_id=user_id).all()
    return render_template('test_list.html', message=message, tests=tests, delete_form=DeleteForm())
