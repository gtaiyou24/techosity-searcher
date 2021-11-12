import dataclasses


@dataclasses.dataclass(init=True, unsafe_hash=True, frozen=True)
class RequestCreateBlog:
    id: str
    title: str
    description: str
    url: str
