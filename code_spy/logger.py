import logging

from colorama import Fore, Style

from code_spy._version import __version__

# Override 3rd party logging
logging.getLogger("fsevents").setLevel(logging.WARNING)
# logging.getLogger("pylint").setLevel(logging.WARNING)
logging.getLogger("pytest").setLevel(logging.WARNING)
logging.getLogger("mypy").setLevel(logging.WARNING)


BOLD = "\033[1m"
RESET_BOLD = "\033[22m"


class CustomFormatter(logging.Formatter):
    _datefmt = "%Y-%m-%d %H:%M:%S"
    error_format = f"{Fore.RED} [code-spy] %(message)s{Style.RESET_ALL}"
    debug_format = f"{Fore.YELLOW}[code-spy] %(message)s{Style.RESET_ALL}"
    info_format = f"{Fore.YELLOW}[code-spy %(asctime)s] %(message)s{Style.RESET_ALL}"

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

def log_task_info(task_name: str, message: str, color: str):
    log.info(f"{Fore.GREEN}✔ {color}[{BOLD}{task_name}{RESET_BOLD}] {Fore.GREEN}{message}{Style.RESET_ALL}")

def log_task_warning(task_name: str, message: str, color: str):
    log.warning(f"{Fore.BLUE}⚠️ {color}[{BOLD}{task_name}{RESET_BOLD}] {Fore.BLUE}{message}{Style.RESET_ALL}")

def log_task_error(task_name: str, message: str, color: str):
    log.info(f"{Fore.RED}✖ {color}[{BOLD}{task_name}{RESET_BOLD}] {Fore.RED}{message}{Style.RESET_ALL}")

def preamble_log():

    print(f"""{Fore.CYAN}
 ██████╗ ██████╗ ██████╗ ███████╗    ███████╗██████╗ ██╗   ██╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██╔════╝██╔══██╗╚██╗ ██╔╝
██║     ██║   ██║██║  ██║█████╗      ███████╗██████╔╝ ╚████╔╝ 
██║     ██║   ██║██║  ██║██╔══╝      ╚════██║██╔═══╝   ╚██╔╝  
╚██████╗╚██████╔╝██████╔╝███████╗    ███████║██║        ██║   
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝        ╚═╝  {__version__} 
    {Fore.RESET}""")
