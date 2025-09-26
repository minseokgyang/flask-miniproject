from app.models import Review
from app import SessionLocal

def get_all_reviews():
    # 모든 리뷰 조회
    db = SessionLocal()
    reviews = db.query(Review).all()
    db.close()
    return reviews

def get_review(review_id):
    # 리뷰생성
    db = SessionLocal()
    review = db.query(Review).get(review_id)
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
    db.commit()
    db.refresh(review)
    db.close()
    return review

def delete_review(review_id):
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
    db = SessionLocal()
    ratings = db.query(Review.rating).all()
    db.close()
    if not ratings:
        return 0
    avg = sum(r[0] for r in ratings) / len(ratings)
    return round(avg, 2)
