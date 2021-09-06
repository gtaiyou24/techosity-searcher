from typing import List

from injector import singleton, inject

from application.blog.dpo import BlogListDpo
from domain.model.blog import BlogRepository, BlogId


@singleton
class BlogApplicationService:

    @inject
    def __init__(self, blog_repository: BlogRepository):
        self.__blog_repository = blog_repository

    def get_list(self, id_list: List[str]) -> BlogListDpo:
        id_list = [BlogId(id) for id in id_list]
        blog_list = self.__blog_repository.blog_list_of(id_list)
        return BlogListDpo(blog_list)
