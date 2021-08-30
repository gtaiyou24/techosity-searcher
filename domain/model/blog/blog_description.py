from dataclasses import dataclass


@dataclass(init=False, frozen=True, unsafe_hash=True)
class BlogDescription:
    text: str

    def __init__(self, text: str):
        assert text is not None, "引数textにNoneが指定されています。引数textは必須です。"
        assert text != "", "引数textに空文字が指定されています。引数textは必須です。"
        assert isinstance(text, str), "引数textに{}が指定されています。文字列を指定して下さい。".format(type(text))
        super().__setattr__("text", text)
