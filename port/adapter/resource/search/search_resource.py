from flask import Blueprint, render_template, request

from application.blog import BlogApplicationService
from application.search import SearchApplicationService
from di import DIManager

SearchResource = Blueprint('search', __name__, url_prefix='/search')

di_manager = DIManager()
search_application_service = di_manager.get(SearchApplicationService)
blog_application_service = di_manager.get(BlogApplicationService)


@SearchResource.route('/')
def search() -> str:
    q: str = str(request.args.get("q"))
    start: int = int(request.args.get("start", 0))

    searched_blog_ids_dpo = search_application_service.search_blog(q, start)
    blog_list_dpo = blog_application_service.get_list(searched_blog_ids_dpo.ids())

    model: dict = {
        'q': q,
        'prev': max(start - 10, 0),
        'next': start + 10,
        'blog_list': [blog_dpo.to_dict() for blog_dpo in blog_list_dpo.list]
    }
    return render_template("search.html", **model)
