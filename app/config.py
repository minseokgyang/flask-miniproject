import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(os.path.dirname(BASE_DIR), "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(INSTANCE_DIR, 'reviews.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True