from flask import Blueprint, render_template, request, redirect, url_for
from app.services.review_service import (
    get_all_reviews, get_review, create_review,
    update_review, delete_review, get_average_rating
)

review_bp = Blueprint("reviews", __name__)


@review_bp.route("/")
def index():
    # 리뷰목록 + 리뷰 평균 별점
    reviews = get_all_reviews()
    avg_rating = get_average_rating()
    return render_template("index.html", reviews=reviews, avg_rating=avg_rating)

 
@review_bp.route("/new", methods=["GET", "POST"])
def new_review():
    # 새로운 리뷰 작성하기
    if request.method == "POST":
        data = {
            "title": request.form["title"],
            "content": request.form["content"],
            "rating": request.form["rating"],
        }
        create_review(data)
        return redirect(url_for("reviews.index"))
    return render_template("new.html")


    # 200 -> 성공~!
    # 201 -> created: 무에서 유 창조
    # 204 -> no content:  뭔가 성공을 했는데 딱히 응답을 할것이 없을때.



@review_bp.route("/edit/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    # 작성했던 리뷰 수정하기
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





@review_bp.route("/delete/<int:review_id>", methods=["POST"])
def delete_review_route(review_id):
    # 리뷰 삭제하기
    delete_review(review_id)
    return redirect(url_for("reviews.index"))
