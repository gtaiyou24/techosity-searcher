import abc
from typing import Optional, List, NoReturn

from domain.model.blog import BlogId, Blog


class BlogRepository(abc.ABC):

    @abc.abstractmethod
    def blog_of(self, id: BlogId) -> Optional[Blog]:
        pass

    @abc.abstractmethod
    def blog_list_of(self, id_list: List[BlogId]) -> List[Blog]:
        pass

    @abc.abstractmethod
    def save(self, blog: Blog) -> NoReturn:
        pass
