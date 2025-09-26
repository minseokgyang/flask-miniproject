from flask import Blueprint, render_template, request, redirect, url_for
from app.services.review_service import (
    get_all_reviews, get_review, create_review,
    update_review, delete_review, get_average_rating
)

review_bp = Blueprint("reviews", __name__)


@review_bp.route("/")
def index():
    # 메인 index.html에서 모든 리뷰와 평균별점을 보여줍니다.
    reviews = get_all_reviews()
    avg_rating = get_average_rating()
    return render_template("index.html", reviews=reviews, avg_rating=avg_rating)

 
@review_bp.route("/new", methods=["GET", "POST"])
def new_review():
    # 리뷰 작성하기 
    # 메소드 GET과 POST를 받아서
    # GET으로는 작성페이지(빈폼)을 보여주고
    # POST로는 사용자가 작성한 리뷰를 받아서 create_review에 저장 후에 메인으로 이동 시켜줍니다.
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
    # 리뷰 수정 및 업데이트
    # 이곳에서도 GET과 POST를 받고 
    # 이 코드에서의 GET은 기존 리뷰 내용을 불러와서 수정폼에 채우는 역할을 합니다.
    # 이 코드에서의 POST는 사용자가 수정한 내용을 받아서 edit.html에 출력 할 수 있게 해줍니다.
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
    # 이 코드에서는 삭제버튼을 누르면 삭제가 되겠끔 작성하였습니다.
    delete_review(review_id)
    return redirect(url_for("reviews.index"))
