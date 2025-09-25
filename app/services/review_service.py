from ..models import Review
from .. import SessionLocal

def get_all_reviews():
    db = SessionLocal()
    reviews = db.query(Review).all()
    db.close()
    return reviews

def get_review(review_id):
    db = SessionLocal()
    review = db.query(Review).get(review_id)
    db.close()
    return review

def create_review(data):
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
