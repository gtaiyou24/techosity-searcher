import abc
from typing import NoReturn


class ExchangeListener(abc.ABC):

    @abc.abstractmethod
    def queue_name(self) -> str:
        pass

    @abc.abstractmethod
    def filtered_dispatch(self, text_message: str) -> NoReturn:
        """受信したメッセージを処理する"""
        pass
