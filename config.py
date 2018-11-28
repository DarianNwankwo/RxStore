import os
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = f"{basedir}/databases"

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "rxstore-like-no-other-baby-but-seriously-set-a-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or f"sqlite:///{os.path.join(db_path)}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False