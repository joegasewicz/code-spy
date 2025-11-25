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
        watch_path=".",
        tasks=[
            MyPyTask(path="examples/routes", mypy_file="examples/mypy.ini"),
            PylintTask(path="examples/routes", rcfile="examples/.pylintrc"),
            PytestTask(path="examples/tests"),
            BlackTask(path="examples/routes"),
            DevServerTask(wsgi_app=bobtail),
        ],
    )
    dr.watch()
