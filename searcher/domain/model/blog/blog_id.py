from dataclasses import dataclass


@dataclass(init=False, frozen=True, unsafe_hash=True)
class BlogId:
    id: str

    def __init__(self, id: str):
        assert id is not None, "引数idにNoneが指定されました。引数idは必須です。"
        assert id != '', "引数idに空文字が指定されました。引数idは必須です。"
        assert isinstance(id, str), "引数idには文字列を指定して下さい。"
        super().__setattr__("id", id)
