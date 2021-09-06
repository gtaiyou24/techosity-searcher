from dataclasses import dataclass


@dataclass(init=False, frozen=True, unsafe_hash=True)
class BlogTitle:
    title: str

    def __init__(self, title: str):
        assert title is not None, "引数titleにNoneが指定されています。引数titleは必須です。"
        assert title != '', "引数titleに空文字が指定されています。引数titleは必須です。"
        assert isinstance(title, str), "引数titleには文字列を指定して下さい。"
        super().__setattr__("title", title)
