from dataclasses import dataclass
from typing import List

from application.blog.dpo import BlogDpo
from domain.model.blog import Blog


@dataclass(init=False, frozen=True, unsafe_hash=True)
class BlogListDpo:
    list: List[BlogDpo]

    def __init__(self, blog_list: List[Blog]):
        super().__setattr__("list", [BlogDpo(blog) for blog in blog_list])
