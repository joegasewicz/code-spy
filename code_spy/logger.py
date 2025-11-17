import logging

from colorama import Fore, Style

from code_spy._version import __version__

# Override 3rd party logging
logging.getLogger("fsevents").setLevel(logging.WARNING)


class CustomFormatter(logging.Formatter):
    _datefmt = "%Y-%m-%d %H:%M:%S"
    error_format = f"{Fore.RED}✖ [code-spy] %(message)s{Style.RESET_ALL}"
    debug_format = f"{Fore.BLUE}[code-spy] %(message)s{Style.RESET_ALL}"
    info_format = f"{Fore.GREEN}✔ [code-spy %(asctime)s] %(message)s{Style.RESET_ALL}"

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
log.handlers = []   # To stop duplicate logging
log.addHandler(handler)
log.propagate = False
# log.setLevel(logging.INFO)


def preamble_log():

    print(f"""{Fore.CYAN}
 ██████╗ ██████╗ ██████╗ ███████╗    ███████╗██████╗ ██╗   ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██╔════╝██╔══██╗╚██╗ ██╔╝
██║     ██║   ██║██║  ██║█████╗      ███████╗██████╔╝ ╚████╔╝ 
██║     ██║   ██║██║  ██║██╔══╝      ╚════██║██╔═══╝   ╚██╔╝  
╚██████╗╚██████╔╝██████╔╝███████╗    ███████║██║        ██║   
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝        ╚═╝  {__version__} 
    {Fore.RESET}""")
