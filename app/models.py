from sqlalchemy import Column, Integer, String
from . import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)   # 책/영화 이름
    content = Column(String, nullable=False) # 리뷰 내용
    rating = Column(Integer, nullable=False) # 별점 (1~5)

    def __repr__(self):
        return f"<Review(id={self.id}, title='{self.title}', rating={self.rating})>"
