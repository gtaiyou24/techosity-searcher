from __future__ import annotations

from enum import Enum

from logger import log


class ErrorLevel(Enum):
    WARN = 'WARN'
    ERROR = 'ERROR'
    CRITICAL = 'CRITICAL'

    def to_logger(self, error_code: ErrorCode, detail: str):
        msg = "[Code] {code} [Message] {message} [Detail] {detail}".format(
            code=error_code.name, message=error_code.message, detail=detail)

        if self == ErrorLevel.WARN:
            log.warn(msg)
        elif self == ErrorLevel.ERROR:
            log.error(msg)
        elif self == ErrorLevel.CRITICAL:
            log.critical(msg)
        else:
            log.info(msg)


class ErrorCode(Enum):
    COMMON_1001 = ('内部エラーが発生しました。', ErrorLevel.CRITICAL)

    DB_CAN_NOT_CONNECT_TO_DATABASE = ('データベースへの接続に失敗しました。', ErrorLevel.CRITICAL)
    DB_CLIENT_ERROR = ('クライアントエラーが発生しました。', ErrorLevel.ERROR)
    DB_NOT_FOUND = ('該当データが見つかりません。', ErrorLevel.ERROR)
    DB_TIME_OUT = ('タイムアウトが発生しました。', ErrorLevel.WARN)

    def __init__(self, message: str, error_level: ErrorLevel):
        self.message = message
        self.error_level = error_level

    def log(self, detail: str):
        self.error_level.to_logger(self, detail)
