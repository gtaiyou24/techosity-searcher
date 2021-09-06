from dataclasses import dataclass
from typing import List

from domain.model.blog import BlogId


@dataclass(init=False, frozen=True, unsafe_hash=True)
class SearchedBlogIdsDpo:
    _blog_id_list: List[BlogId]

    def __init__(self, blog_id_list: List[BlogId]):
        assert blog_id_list is not None, "引数blog_id_listは必須です。"
        super().__setattr__("_blog_id_list", blog_id_list)

    def ids(self) -> List[str]:
        return [blog_id.id for blog_id in self._blog_id_list]
