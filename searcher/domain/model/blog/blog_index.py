import abc
from typing import List, NoReturn

from domain.model.blog import Blog


class BlogIndex(abc.ABC):

    @abc.abstractmethod
    def search(self, query: str, start: int) -> List[Blog]:
        pass

    @abc.abstractmethod
    def add(self, blog: Blog) -> NoReturn:
        pass
