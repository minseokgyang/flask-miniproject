import os


INSTANCE_DIR = os.path.join(os.path.dirname(__file__),"..", "instance")
#instance 폴더안에 실제 데이터(DB)를 저장해둠
os.makedirs(INSTANCE_DIR, exist_ok=True)
#없다면 자동으로 만들어주게 만든것.

class Config:
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(INSTANCE_DIR, 'reviews.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

#SQLALchemy_DATABASE_URI은 DB파일 경로 즉, review.db를 칭한것
#SQLAlchemy_TRACK_MODIFICATIONS은 DB를 변경 감시를 끄게 만든것입니다(인터넷에서 찾아온것..)
#DEBUG를 True 개발모드를 켜서 에러및 변경사항을 쉽게 볼 수 있게 했습니다.