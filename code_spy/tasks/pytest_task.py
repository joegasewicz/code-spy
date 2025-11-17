import sys
import importlib

import pytest

from code_spy.tasks.base_task import BaseTask
from code_spy.logger import log


class PytestTask(BaseTask):

    def __init__(self, *, path: str = None, args: list[str] = None):
        self.path = path
        self.args = args

    def run(self) -> None:
        args = []
        if self.path:
            args.append(self.path)
        args.append("--cache-clear")
        if self.args:
            args.append(*self.args)
        log.info("[pytest] Starting pytest...")

        for name, module in list(sys.modules.items()):
            if name.startswith(self.path.replace("/", ".")):
                importlib.reload(module)
        exit_code = pytest.main(args)


    def stop(self) -> None:
        pass