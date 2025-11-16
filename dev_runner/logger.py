import logging

from colorama import Fore, Style

# Override 3rd party logging
logging.getLogger("fsevents").setLevel(logging.WARNING)


class CustomFormatter(logging.Formatter):
    _datefmt = "%Y-%m-%d %H:%M:%S"
    error_format = f"{Fore.RED}✖ [dev-runner] %(message)s{Style.RESET_ALL}"
    debug_format = f"{Fore.BLUE}[dev-runner] %(message)s{Style.RESET_ALL}"
    info_format = f"{Fore.GREEN}✔ [dev-runner %(asctime)s] %(message)s{Style.RESET_ALL}"

    def __init__(self):
        super().__init__(fmt="%(levelno)d: %(msg)s", datefmt=None, style="%")

    def format(self, record):
        self.datefmt = self._datefmt
        if record.levelno == logging.INFO:
            self._style._fmt = CustomFormatter.info_format

        elif record.levelno == logging.DEBUG:
            self._style._fmt = CustomFormatter.debug_format

        elif record.levelno == logging.ERROR:
            self._style._fmt = CustomFormatter.error_format

        result = logging.Formatter.format(self, record)
        return result


formatter = CustomFormatter()
handler = logging.StreamHandler()
handler.setFormatter(formatter)

log = logging.getLogger(__name__)
log.addHandler(handler)
# log.setLevel(logging.INFO)
