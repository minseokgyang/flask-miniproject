from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import Config

# SQLAlchemy 설정
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

def create_app():
    from .routes.review_routes import review_bp
    from .models import Review

    # DB 테이블 생성
    Base.metadata.create_all(bind=engine)

    # Flask 앱 생성
    app = Flask(__name__)
    app.config.from_object(Config)

    # 블루프린트 등록
    app.register_blueprint(review_bp)

    return app
