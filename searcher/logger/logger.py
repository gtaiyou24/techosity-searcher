import os
from logging import getLogger, StreamHandler, Formatter, getLevelName

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
level = getLevelName(LOG_LEVEL)

log = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(level)
handler.setFormatter(Formatter("[%(levelname)s] [%(asctime)s] [%(filename)s:%(lineno)d] %(message)s"))
log.setLevel(level)
log.addHandler(handler)
log.propagate = False
