from typing import Type

from injector import Injector, T

from di import DI
from domain.model.blog import BlogIndex, BlogRepository
from port.adapter.persistence.repository.blog import InMemoryBlogRepository
from port.adapter.persistence.searchengine.elasticsearch.blog import ElasticSearchBlogIndex
from port.adapter.persistence.searchengine.inmemory.blog import InMemoryBlogIndex


class DIManager:

    def __init__(self):
        self.__injector = Injector([
            # Blog
            DI.new(BlogIndex, {"elasticsearch": ElasticSearchBlogIndex, "inmemory": InMemoryBlogIndex}),
            DI.new(BlogRepository, {"inmemory": InMemoryBlogRepository}, InMemoryBlogRepository)
        ])

    def get(self, interface: Type[T]) -> T:
        return self.__injector.get(interface)
