from typing import NoReturn, List

from elasticsearch import Elasticsearch

from domain.model.blog import Blog, BlogIndex
from exception import SystemException, ErrorCode
from logger import log


class ElasticSearchBlogIndex(BlogIndex):
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

        blog_list = []
        for document in search_result['hits']['hits']:
            blog_list.append(Blog.of(
                str(document['_id']), str(document['_source']['title']),
                str(document['_source']['description']), str(document['_source']['url'])))

        return blog_list

    def add(self, blog: Blog) -> NoReturn:
        log.debug("BlogをElasticSearchに保存します")
        # ドキュメントの登録
        result = self.__client.create(
            index=self.INDEX_NAME, id=blog.id(),
            body={"title": blog.title(), "description": blog.description(), "url": blog.url()}
        )
        log.debug("{}".format(result))
