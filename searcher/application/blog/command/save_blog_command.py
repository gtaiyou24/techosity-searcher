from dataclasses import dataclass


@dataclass(init=True, frozen=True, unsafe_hash=True)
class SaveBlogCommand:
    blog_id: str
    blog_title: str
    blog_description: str
    url: str
