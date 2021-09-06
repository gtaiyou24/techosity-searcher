from flask import Blueprint, render_template, request

from application.search import SearchApplicationService
from di import DIManager

SearchResource = Blueprint('search', __name__, url_prefix='/search')

di_manager = DIManager()
search_application_service = di_manager.get(SearchApplicationService)


@SearchResource.route('/')
def search() -> str:
    q: str = str(request.args.get("q"))
    start: int = int(request.args.get("start", 0))

    searched_blogs_dpo = search_application_service.search_blog(q, start)

    model: dict = {
        'q': q,
        'prev': max(start - 10, 0),
        'next': start + 10,
        'blog_list': [blog for blog in searched_blogs_dpo.blog_list()]
    }
    return render_template("search.html", **model)
