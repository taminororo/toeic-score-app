from flask import Flask
from models import db
from flask_migrate import Migrate
from routes.test import test_bp
from routes.auth import auth_bp
from flask_wtf import CSRFProtect # CSRF対策用の拡張ライブラリ
from dotenv import load_dotenv
import os
from config import DevelopmentConfig, ProductionConfig

load_dotenv()   # .envから環境変数を読み込む（ローカル開発用）

app = Flask(__name__, instance_relative_config=True)

# FLASK_ENVで判定
env = os.getenv("FLASK_ENV", "production") == "1"

# 設定を切り替えて適用
if env == "development":
    app.config.from_object(DevelopmentConfig)
else:
    app.config.from_object(ProductionConfig)

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



