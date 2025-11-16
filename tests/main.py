from bobtail import BobTail, AbstractRoute, Request, Response
from bobtail_logger import BobtailLogger

from dev_runner import DevRunner, MyPyTask, DevServerTask


from tests.routes import HomeRoute


routes = [
    (HomeRoute(), "/")
]

if __name__ == "__main__":
    bobtail = BobTail(routes=routes)
    bobtail.use(BobtailLogger())
    dr = DevRunner(
        path=".",
        tasks=[
            MyPyTask(path="routes", mypy_file="mypy.ini"),
            DevServerTask(wsgi_app=bobtail),
        ]
    )
    dr.watch()
