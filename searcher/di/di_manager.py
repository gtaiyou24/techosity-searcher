from typing import Type

from injector import Injector, T

from di import DI
from domain.model.blog import BlogSearcher
from port.adapter.persistence.searcher.elasticsearch.blog import ElasticSearchBlogSearcher
from port.adapter.persistence.searcher.inmemory.blog import InMemoryBlogSearcher


class DIManager:

    def __init__(self):
        self.__injector = Injector([
            # Blog
            DI.new(BlogSearcher, {"elasticsearch": ElasticSearchBlogSearcher, "inmemory": InMemoryBlogSearcher}),
            # DI.new(BlogRepository, {"inmemory": InMemoryBlogRepository})
        ])

    def get(self, interface: Type[T]) -> T:
        return self.__injector.get(interface)
