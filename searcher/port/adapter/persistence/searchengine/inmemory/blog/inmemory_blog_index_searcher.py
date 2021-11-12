from typing import List, NoReturn, Set

from domain.model.blog import BlogIndex, Blog


class InMemoryBlogIndex(BlogIndex):
    __blogs: Set[Blog] = set()

    def search(self, query: str, start: int) -> List[Blog]:
        result_blog_list = []
        for blog in self.__blogs:
            if query in blog.title():
                result_blog_list.append(blog)
        return result_blog_list

    def add(self, blog: Blog) -> NoReturn:
        self.__blogs.add(blog)
