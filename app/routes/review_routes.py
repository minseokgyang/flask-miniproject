from flask import Blueprint, render_template, request, redirect, url_for
from ..services.review_service import (
    get_all_reviews, get_review, create_review,
    update_review, delete_review, get_average_rating
)

review_bp = Blueprint("reviews", __name__)

# 리뷰 목록만들기 평균 별점만들기
@review_bp.route("/")
def index():
    reviews = get_all_reviews()
    avg_rating = get_average_rating()
    return render_template("index.html", reviews=reviews, avg_rating=avg_rating)

# 리뷰 작성하기 
@review_bp.route("/new", methods=["GET", "POST"])
def new_review():
    if request.method == "POST":
        data = {
            "title": request.form["title"],
            "content": request.form["content"],
            "rating": request.form["rating"],
        }
        create_review(data)
        return redirect(url_for("reviews.index"))
    return render_template("new.html")

# 리뷰 수정하기
@review_bp.route("/edit/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = get_review(review_id)
    if not review:
        return "리뷰를 찾을 수 없습니다", 404

    if request.method == "POST":
        data = {
            "title": request.form["title"],
            "content": request.form["content"],
            "rating": request.form["rating"],
        }
        update_review(review_id, data)
        return redirect(url_for("reviews.index"))
    return render_template("edit.html", review=review)

# 리뷰 삭제하기
@review_bp.route("/delete/<int:review_id>", methods=["POST"])
def delete_review_route(review_id):
    delete_review(review_id)
    return redirect(url_for("reviews.index"))
