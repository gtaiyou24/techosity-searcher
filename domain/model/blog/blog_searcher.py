import abc
from typing import List

from domain.model.blog import BlogId


class BlogSearcher(abc.ABC):

    @abc.abstractmethod
    def search(self, query: str, start: int) -> List[BlogId]:
        pass
