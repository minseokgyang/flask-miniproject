from sqlalchemy import Column, Integer, String
from . import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True) #고유이름
    title = Column(String, nullable=False)   # 책/영화 이름
    content = Column(String, nullable=False) # 리뷰 내용
    rating = Column(Integer, nullable=False) # 별점 (1~5)

    def __repr__(self):
        return f"<Review(id={self.id}, title='{self.title}', rating={self.rating})>"

#DB에 리뷰 라는 테이블을 만들고, 테이블의 값을 정한 코드입니다.