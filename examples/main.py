from bobtail import BobTail, AbstractRoute, Request, Response
from bobtail_logger import BobtailLogger
from code_spy.core import CodeSpy
from code_spy.tasks import (
    MyPyTask,
    DevServerTask,
    PylintTask,
    PytestTask,
    BlackTask,
)

from examples.routes import HomeRoute


routes = [(HomeRoute(), "/")]

if __name__ == "__main__":
    bobtail = BobTail(routes=routes)
    bobtail.use(BobtailLogger())
    dr = CodeSpy(
        path=".",
        tasks=[
            MyPyTask(path="routes", mypy_file="mypy.ini"),
            PylintTask(path="routes", rcfile=".pylintrc"),
            PytestTask(path="tests"),
            BlackTask(path="routes"),
            DevServerTask(wsgi_app=bobtail),
        ],
    )
    dr.watch()
