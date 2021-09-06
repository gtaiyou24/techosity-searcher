import abc
from typing import List

from domain.model.blog import Blog


class BlogSearcher(abc.ABC):

    @abc.abstractmethod
    def search(self, query: str, start: int) -> List[Blog]:
        pass
