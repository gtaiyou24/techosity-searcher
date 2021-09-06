from typing import List

from injector import inject, singleton

from application.search.dpo import SearchedBlogsDpo
from domain.model.blog import BlogSearcher, Blog


@singleton
class SearchApplicationService:

    @inject
    def __init__(self, blog_searcher: BlogSearcher):
        self.__blog_searcher = blog_searcher

    def search_blog(self, query: str, start: int) -> SearchedBlogsDpo:
        """
        2. クエリ指定でindexからブログを検索し、ブログを取得する
        3. ブログを返却する

        :param query:
        :param start:
        :return:
        """
        blog_list: List[Blog] = self.__blog_searcher.search(query, start)
        return SearchedBlogsDpo(blog_list)
