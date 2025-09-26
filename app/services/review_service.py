from app.models import Review
from app import SessionLocal

def get_all_reviews():
    # 모든 리뷰 조회
    
    db = SessionLocal()
    reviews = db.query(Review).all()
    #DB에 있는 모든 리뷰를 리스트로 가져옵니다.
    db.close()
    return reviews

def get_review(review_id):
    # 특정 리뷰 가져오기
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    #id로 원하는 리뷰를 1개 찾는 코드입니다.
    db.close()
    return review

def create_review(data):
    # 리뷰 생성
    db = SessionLocal()
    new_review = Review(
        title=data["title"],
        content=data["content"],
        rating=int(data["rating"])
    )
    #사용자가 입력한 제목/내용/별점을 받아서 새 리뷰를 작성하는것을 도와줍니다.
    #그 후엔 DB에 저장 후 반환!
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    db.close()
    return new_review

def update_review(review_id, data):
    # 리뷰 업데이트 
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    if not review:
        db.close()
        return None
    review.title = data["title"]
    review.content = data["content"]
    review.rating = int(data["rating"])
    #제목/내용/별점등을 새 값으로 바꾸고 
    #그 후에 DB에 반영합니다.
    db.commit()
    db.refresh(review)
    db.close()
    return review

def delete_review(review_id):#
    #리뷰 삭제
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    if not review:
        db.close()
        return False
    db.delete(review)
    db.commit()
    db.close()
    return True

def get_average_rating():
    #총 별점을 더해서 평균을 내는 코드입니다.
    db = SessionLocal()
    ratings = db.query(Review.rating).all()
    db.close()
    if not ratings:
        return 0
    avg = sum(r[0] for r in ratings) / len(ratings)
    #sum으로 더하고 ratings에 있는 수만큼 나눠서 평균을 냅니다.
    return round(avg, 2)
