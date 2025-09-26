import os


INSTANCE_DIR = os.path.join(os.path.dirname(__file__)," .. ", "instance")
os.makedirs(INSTANCE_DIR, exist_ok=True)

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(INSTANCE_DIR, 'reviews.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True