# TOEIC スコア管理アプリ（Flask製）

このアプリは、TOEICの模試のスコアをパートごとに記録・管理できるWebアプリです。  
ユーザー登録・ログイン機能付きで、自分だけのスコア履歴を安全に保存できます。

##  主な機能

- ユーザー登録・ログイン（CSRF・セッション対策済み）
- テストスコアの登録（PART1〜7まで入力）
- 正答率の自動計算と表示（リスニング・リーディング・全体の正答率も表示）
- スコア履歴の一覧表示
- 登録内容の確認画面、削除機能あり

##  技術スタック

- Python / Flask
- HTML (Jinja2) + Bootstrap 5
- SQLite（ローカル） or PostgreSQL（本番）
- Flask-WTF（フォーム + CSRF対策）
- Flask-Login（ログイン認証）
- Flask-Migrate（マイグレーション対応）

##  デプロイ方法（Render）

### 1. 必要ファイルを準備

- `requirements.txt`
- `Procfile`
- `.env`（**Gitには含めない**）

### 2. Renderの設定

- [Render](https://render.com) にログイン
- `New Web Service` → GitHubリポジトリを選択
- 以下の設定を入力：

| 項目 | 値 |
|------|----|
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |
| Environment | Python |
| Environment Variables | `SECRET_KEY`, `DATABASE_URL` を追加 |

### 3. PostgreSQLを使う場合

- RenderでDatabase → PostgreSQLを作成
- `DATABASE_URL` を環境変数にコピペ

##  環境変数（例）

SECRET_KEY=your-secret-key-here DATABASE_URL=postgresql://user:pass@host:port/dbname


##  ディレクトリ構成（抜粋）

flask_project/ ├── app.py ├── models.py ├── forms.py ├── routes/ │ ├── auth.py │ └── test.py ├── templates/ │ └── *.html ├── requirements.txt ├── Procfile └── .env 


##  ライセンス

MIT License

---
