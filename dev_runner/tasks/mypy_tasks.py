from mypy import api

from dev_runner.logger import log
from dev_runner.tasks.base_task import BaseTask


class MyPyTask(BaseTask):

    def __init__(self, *, path: str, mypy_file: str = "mypy.ini"):
        self.path = path
        self.mypy_file = mypy_file

    def run(self):
        result = api.run([
            "--strict",
            "--config-file",
            self.mypy_file,
            self.path,
        ])
        std_info = result[0]
        std_error = result[1]

        if std_error:
            std_error = f"[mypy]: {std_error}"
            log.error(std_error)
        elif "error:" in std_info:
            std_info = f"[mypy]: {std_info}"
            log.error(std_info)
        else:
            std_info = f"[mypy]: {std_info}"
            log.info(std_info)
