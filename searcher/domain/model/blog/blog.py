from __future__ import annotations

from dataclasses import dataclass

from domain.model.blog import BlogId, BlogTitle, BlogDescription
from domain.model.url import URL


@dataclass(init=False, frozen=True, unsafe_hash=True)
class Blog:
    blog_id: BlogId
    blog_title: BlogTitle
    blog_description: BlogDescription
    blog_url: URL

    def __init__(self, blog_id: BlogId, blog_title: BlogTitle, blog_description: BlogDescription, url: URL):
        assert blog_id is not None, "引数blog_idにNoneが指定されています。引数blog_idは必須です。"
        assert blog_title is not None, "引数blog_titleにNoneが指定されています。引数blog_titleは必須です。"
        assert blog_description is not None, "引数blog_descriptionにNoneが指定されています。引数blog_descriptionは必須です。"
        assert url is not None, "引数urlにNoneが指定されています。引数urlは必須です。"
        assert isinstance(blog_id, BlogId), \
            "引数blog_idに{}が指定されています。BlogId型を指定して下さい。".format(type(blog_id))
        assert isinstance(blog_title, BlogTitle), \
            "引数blog_titleに{}が指定されています。BlogTitle型を指定して下さい。".format(type(blog_title))
        assert isinstance(blog_description, BlogDescription), \
            "引数blog_descriptionに{}が指定されています。BlogDescription型を指定して下さい。".format(type(blog_description))
        assert isinstance(url, URL), "引数urlに{}が指定されています。URL型を指定して下さい。".format(type(url))
        super().__setattr__("blog_id", blog_id)
        super().__setattr__("blog_title", blog_title)
        super().__setattr__("blog_description", blog_description)
        super().__setattr__("blog_url", url)

    @staticmethod
    def of(id: str, title: str, description: str, url: str) -> Blog:
        return Blog(BlogId(id), BlogTitle(title), BlogDescription(description), URL(url))

    def id(self) -> str:
        return self.blog_id.id

    def title(self) -> str:
        return self.blog_title.title

    def description(self) -> str:
        return self.blog_description.text

    def url(self) -> str:
        return self.blog_url.absolute_url
