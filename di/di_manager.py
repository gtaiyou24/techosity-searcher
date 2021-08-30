from typing import Type

from injector import Injector, T

from di import Setter, Profile
from domain.model.blog import BlogSearcher, BlogRepository
from port.adapter.persistence.repository.blog import InMemoryBlogRepository
from port.adapter.persistence.searcher.blog import InMemoryBlogSearcher


class DIManager:

    def __init__(self):
        self.__injector = Injector([
            # Blog
            Setter(BlogSearcher, {Profile({"inmemory"}): InMemoryBlogSearcher}),
            Setter(BlogRepository, {Profile({"inmemory"}): InMemoryBlogRepository})
        ])

    def get(self, interface: Type[T]) -> T:
        return self.__injector.get(interface)
