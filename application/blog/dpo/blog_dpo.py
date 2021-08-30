from dataclasses import dataclass

from domain.model.blog import Blog


@dataclass(init=True, frozen=True, unsafe_hash=True)
class BlogDpo:
    blog: Blog

    def to_dict(self) -> dict:
        return {
            "id": self.blog.id(),
            "title": self.blog.title(),
            "description": self.blog.description(),
            "url": self.blog.url()
        }
