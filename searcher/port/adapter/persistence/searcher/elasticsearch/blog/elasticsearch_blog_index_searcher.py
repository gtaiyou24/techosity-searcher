from typing import NoReturn, List

from elasticsearch import Elasticsearch

from domain.model.blog import Blog, BlogSearcher
from exception import SystemException, ErrorCode
from logger import log


class ElasticSearchBlogSearcher(BlogSearcher):
    INDEX_NAME = 'blogs'

    def __init__(self):
        self.__client = Elasticsearch('elasticsearch')

        # インデックスの存在確認
        if not self.__client.indices.exists(index=self.INDEX_NAME):
            raise SystemException(ErrorCode.DB_CLIENT_ERROR,
                                  "ElasticSearchのインデックスに{}がありませんでした。".format(self.INDEX_NAME))

    def search(self, query: str, start: int) -> List[Blog]:
        log.debug("ElasticSearchで「{}」を検索します".format(query))
        search_result = self.__client.search(
            index=self.INDEX_NAME,
            body={
                'query': {
                    'match': {
                        'title': query
                    }
                }
            },
            size=10,
            from_=start
        )

        log.debug(search_result)

        for document in search_result['hits']['hits']:
            print(document)

        return [Blog.of(str(i), 'title is ' + str(i), 'desc ' + str(i), 'http://hoge.com/blogs/' + str(i)) for i in range(1 + start, 11 + start)]
