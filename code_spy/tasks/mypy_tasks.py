import textwrap

from mypy import api
from colorama import Fore

from code_spy.logger import log_task_info, log_task_error
from code_spy.tasks.base_task import BaseTask


class MyPyTask(BaseTask):

    def __init__(
        self,
        *,
        path: str,
        mypy_file: str = "mypy.ini",
        full_logs: bool = False,
    ):
        self.path = path
        self.mypy_file = mypy_file
        self.full_logs = full_logs

    def run(self, *, log_length: int, src_path: str):

        result = api.run([
            "--strict",
            "--config-file",
            self.mypy_file,
            self.path,
        ])
        std_info = result[0]
        std_error = result[1]

        msg_log = std_error or std_info

        if "error:" in msg_log:
            if self.full_logs:
                log_task_error("mypy", msg_log, Fore.CYAN)
            else:
                msg = textwrap.shorten(msg_log, width=log_length, placeholder="...")
                log_task_error("mypy", msg, Fore.CYAN)
        else:
            msg = textwrap.shorten(msg_log, width=log_length, placeholder="...")
            log_task_info("mypy", msg, Fore.CYAN)

    def stop(self) -> None:
        pass
