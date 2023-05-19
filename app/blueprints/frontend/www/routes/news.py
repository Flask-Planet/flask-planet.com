from flask import render_template, request

from app.models.news import News
from .. import bp


@bp.route("/news", methods=["GET"])
def news():
    news_ = News.all_newest_first_pages(
        page=int(request.args.get("page", 1)),
        per_page=4,
    )

    url_args = {}

    if "page" in request.args:
        url_args["page"] = request.args["page"]

    return render_template(
        bp.tmpl("news.html"),
        news=news_,
        page=news_.page,
        pages=news_.pages,
        url_args=url_args,
    )
