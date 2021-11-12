import json
from typing import NoReturn

from flask import Blueprint, render_template, request, jsonify

from application.blog import BlogApplicationService
from application.blog.command import SaveBlogCommand
from application.search import SearchApplicationService
from di import DIManager
from port.adapter.resource.blog.request import RequestCreateBlog

BlogResource = Blueprint('blog', __name__, url_prefix='/blogs')

di_manager = DIManager()
blog_application_service = di_manager.get(BlogApplicationService)
search_application_service = di_manager.get(SearchApplicationService)


@BlogResource.route('/', methods=['POST'])
def create() -> NoReturn:
    request_create_blog = RequestCreateBlog(**request.get_json())
    save_blog_command = SaveBlogCommand(
        request_create_blog.id, request_create_blog.title, request_create_blog.description, request_create_blog.url)
    blog_application_service.save(save_blog_command)
    return jsonify({"status": "ok"})


@BlogResource.route('/search')
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
