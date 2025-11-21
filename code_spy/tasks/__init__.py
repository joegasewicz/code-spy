from typing import TYPE_CHECKING

from code_spy.tasks.base_task import BaseTask
from code_spy.tasks.mypy_tasks import MyPyTask
from code_spy.tasks.dev_server_task import DevServerTask
from code_spy.tasks.pylint_task import PylintTask
from code_spy.tasks.pytest_task import PytestTask
from code_spy.tasks.black_task import BlackTask

__all__ = [
    "BaseTask",
    "MyPyTask",
    "DevServerTask",
    "PylintTask",
    "PytestTask",
    "BlackTask",
]

if TYPE_CHECKING:
    from .base_task import BaseTask
