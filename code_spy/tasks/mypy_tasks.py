import textwrap

from mypy import api

from code_spy.logger import log
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
                log.error(f"[mypy] {msg_log}")
            else:
                msg = textwrap.shorten(msg_log, width=log_length, placeholder="...")
                msg_log = f"[mypy]: {msg}"
                log.error(msg_log)
        else:
            msg = textwrap.shorten(msg_log, width=log_length, placeholder="...")
            msg_log = f"[mypy]: {msg}"
            log.info(msg_log)

    def stop(self) -> None:
        pass
