from typing import List

from domain.model.blog import BlogSearcher, BlogId


class InMemoryBlogSearcher(BlogSearcher):

    def search(self, query: str, start: int) -> List[BlogId]:
        return [BlogId(str(i)) for i in range(1 + start, 11 + start)]
