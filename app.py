from flask import Flask
from models import db
from flask_migrate import Migrate
from routes.test import test_bp
from routes.auth import auth_bp
from flask_wtf import CSRFProtect # CSRF対策用の拡張ライブラリ
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, instance_relative_config=True)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_scores.db'  # SQLiteのデータベースファイルを指定
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 警告を抑制するための設定
#app.config['SECRET_KEY'] = 'W32eBFv9TbjWeDl6k5j0gKbvNJ3GZJZ7Qm0f0rjObWo'  # セッション用の秘密

#   .envファイルから環境変数を読み込む
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect(app)  # CSRF対策を有効化
db.init_app(app)
migrate = Migrate(app, db)  # Flask-Migrateのインスタンスを作成

# Blueprint 登録
app.register_blueprint(test_bp)
app.register_blueprint(auth_bp)

#初回起動時にデータベースを作成
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)



