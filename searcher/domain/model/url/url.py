from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(init=False, frozen=True, unsafe_hash=True)
class URL:
    absolute_url: str

    def __init__(self, absolute_url: str):
        assert absolute_url is not None, "引数absolute_urlにNoneが指定されています。引数absolute_urlは必須です。"
        assert absolute_url != '', "引数absolute_urlに空文字が指定されています。引数absolute_urlは必須です。"
        assert isinstance(absolute_url, str), \
            "引数absolute_urlに{}が指定されています。引数absolute_urlには文字列を指定して下さい。".format(type(absolute_url))
        assert self.__is_absolute_url(absolute_url), "{}は完全URLではありません。完全URLを指定して下さい。".format(absolute_url)
        super().__setattr__("absolute_url", absolute_url)

    @staticmethod
    def __is_absolute_url(url: str) -> bool:
        return re.match(r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", url) is not None