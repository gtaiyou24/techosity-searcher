from typing import List

from injector import inject, singleton

from application.search.dpo import SearchedBlogIdsDpo
from domain.model.blog import BlogSearcher, BlogId


@singleton
class SearchApplicationService:

    @inject
    def __init__(self, blog_searcher: BlogSearcher):
        self.__blog_searcher = blog_searcher

    def search_blog(self, query: str, start: int) -> SearchedBlogIdsDpo:
        """
        2. クエリ指定でindexからブログを検索し、ブログIDを取得する
        3. ブログIDを返却する

        :param query:
        :param start:
        :return:
        """
        blog_id_list: List[BlogId] = self.__blog_searcher.search(query, start)
        return SearchedBlogIdsDpo(blog_id_list)
