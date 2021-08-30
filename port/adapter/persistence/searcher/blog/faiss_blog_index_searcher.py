from typing import List

from domain.model.blog import BlogSearcher, BlogId


class FaissBlogSearcher(BlogSearcher):

    def search(self, query: str, start: int) -> List[BlogId]:
        pass
