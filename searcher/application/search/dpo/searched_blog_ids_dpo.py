from typing import List

from domain.model.blog import Blog


class SearchedBlogsDpo:

    def __init__(self, blog_list: List[Blog]):
        assert blog_list is not None, "引数blog_id_listは必須です。"
        self.__blog_list = blog_list

    def blog_list(self) -> list[dict[str, str]]:
        return [{'id': blog.id(), 'title': blog.title(), 'description': blog.description(), 'url': blog.url()} \
                for blog in self.__blog_list]
