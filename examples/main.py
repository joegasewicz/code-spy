from bobtail import BobTail, AbstractRoute, Request, Response
from bobtail_logger import BobtailLogger

from code_spy import (
    CodeSpy,
    MyPyTask,
    DevServerTask,
    PylintTask,
    PytestTask,
)

from examples.routes import HomeRoute


routes = [
    (HomeRoute(), "/")
]

if __name__ == "__main__":
    bobtail = BobTail(routes=routes)
    bobtail.use(BobtailLogger())
    dr = CodeSpy(
        path=".",
        tasks=[
            MyPyTask(path="routes", mypy_file="mypy.ini"),
            PylintTask(path="routes", rcfile=".pylintrc"),
            PytestTask(path="tests"),
            DevServerTask(wsgi_app=bobtail),
        ]
    )
    dr.watch()
