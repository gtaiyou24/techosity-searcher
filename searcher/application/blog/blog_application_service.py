from typing import List, NoReturn

from injector import singleton, inject

from application.blog.command import SaveBlogCommand
from application.blog.dpo import BlogListDpo
from domain.model.blog import BlogRepository, BlogId, Blog, BlogIndex
from logger import log


@singleton
class BlogApplicationService:

    @inject
    def __init__(self,
                 blog_repository: BlogRepository,
                 blog_index: BlogIndex):
        self.__blog_repository = blog_repository
        self.__blog_index = blog_index

    def get_list(self, id_list: List[str]) -> BlogListDpo:
        id_list = [BlogId(id) for id in id_list]
        blog_list = self.__blog_repository.blog_list_of(id_list)
        return BlogListDpo(blog_list)

    def save(self, save_blog_command: SaveBlogCommand) -> NoReturn:
        log.debug("CommandからBlogを生成します。")
        blog = Blog.of(
            save_blog_command.blog_id,
            save_blog_command.blog_title,
            save_blog_command.blog_description,
            save_blog_command.url
        )
        log.debug("Blog {} を生成しました".format(blog))

        # TODO : トランザクション
        log.debug("IndexにBlogを保存します")
        self.__blog_index.add(blog)
        log.debug("RepositoryにBlogを保存します")
        self.__blog_repository.save(blog)
