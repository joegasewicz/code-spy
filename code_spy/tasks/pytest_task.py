import sys
import importlib

import pytest

from code_spy.tasks.base_task import BaseTask
from code_spy.logger import log


class PytestLogger:
    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.skipped = 0
        self.failed_reports = []

    def pytest_runtest_logreport(self, report):
        if report.when == "call":
            if report.passed:
                self.passed += 1
            elif report.failed:
                self.failed += 1
                self.failed_reports.append(report)
            elif report.skipped:
                self.skipped += 1

    def pytest_sessionfinish(self, session, exitstatus):
        if self.failed > 0:
            msg = f"[pytest] ✔ {self.passed} passed, ✖ {self.failed} failed, ⚠ {self.skipped} skipped"
            for report in self.failed_reports:
                long_message = report.longrepr
                long_msg = str(long_message).split("_ _ _ _ _")[0]
                msg += f"\n\t✖ {report.nodeid} {long_msg}"
                log.error(msg)
        else:
            log.info(f"[pytest] ✔ {self.passed} passed, ✖ {self.failed} failed, ⚠ {self.skipped} skipped")


class PytestTask(BaseTask):

    def __init__(self, *, path: str = None, args: list[str] = None):
        self.path = path
        self.args = args

    def run(self, *, log_length: int, src_path: str) -> None:
        args = []
        if self.path:
            args.append(self.path)
        args.append("--cache-clear")
        if self.args:
            args.append(*self.args)
        args.append("-p")
        args.append("no:terminalreporter")

        for name, module in list(sys.modules.items()):
            if name.startswith(self.path.replace("/", ".")):
                importlib.reload(module)
        exit_code = pytest.main(args, plugins=[PytestLogger()])


    def stop(self) -> None:
        pass