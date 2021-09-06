from typing import List

from domain.model.blog import BlogSearcher, Blog


class InMemoryBlogSearcher(BlogSearcher):

    def search(self, query: str, start: int) -> List[Blog]:
        return [Blog.of(str(i), 'title is ' + str(i), 'desc ' + str(i), 'http://hoge.com/blogs/' + str(i)) for i in range(1 + start, 11 + start)]
