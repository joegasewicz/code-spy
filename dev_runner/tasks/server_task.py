import threading
from typing import Callable, Iterable, Any, Union
from wsgiref.simple_server import make_server, WSGIRequestHandler

from dev_runner.tasks import BaseTask
from dev_runner.logger import log


WSGICallable = Callable[[dict[str, Any], Any], Iterable[bytes]]


class WSGIServerThread(threading.Thread):

    def __init__(self, app, host, port):
        super().__init__()
        self.app = app
        self.host = host
        self.port = port
        self.server = None

    def run(self):
        log.info("[server task] Starting development Server...")
        self.server = make_server(
            self.host,
            self.port,
            self.app,
            handler_class=WSGIRequestHandler,
        )

        self.server.allow_reuse_address = True
        self.server.serve_forever()

    def stop(self):
        log.info("[server task] Stopping Dev Server...")
        if self.server:
            self.server.shutdown()
            self.server.server_close()


class DevServerTask(BaseTask):

    thread: Union[WSGIServerThread, None] = None

    background = True

    def __init__(
            self,
            *,
            wsgi_app: WSGICallable,
            host: str = "localhost",
            port: int = 8000,
    ):
        self.wsgi_app = wsgi_app
        self.host = host
        self.port = port

    def run(self) -> None:
        if not self.thread:
            self.thread = WSGIServerThread(
                app=self.wsgi_app,
                host=self.host,
                port=self.port,
            )
            self.thread.start()

    def stop(self):
        if self.thread:
            self.thread.stop()
            self.thread.join()
            self.thread = None
