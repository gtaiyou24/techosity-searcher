from typing import Optional, List, Dict, NoReturn

from domain.model.blog import BlogRepository, Blog, BlogId


class InMemoryBlogRepository(BlogRepository):
    __blog_dict: Dict[BlogId, Blog] = {}

    def blog_of(self, id: BlogId) -> Optional[Blog]:
        blog = self.__blog_dict.get(id)
        return blog

    def blog_list_of(self, id_list: List[BlogId]) -> List[Blog]:
        blog_list = []
        for blog_id, blog in self.__blog_dict.items():
            if blog_id in id_list:
                blog_list.append(blog)
        return blog_list

    def save(self, blog: Blog) -> NoReturn:
        self.__blog_dict[blog.blog_id] = blog
