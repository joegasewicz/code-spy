import threading
from typing import Callable, Iterable, Any, Union
from wsgiref.simple_server import make_server, WSGIRequestHandler, WSGIServer

from code_spy.tasks import BaseTask
from code_spy.logger import log


WSGICallable = Callable[[dict[str, Any], Any], Iterable[bytes]]


class QuietWSGIServer(WSGIServer):

    def log_message(self, format, *args):
        return


class QuietHandler(WSGIRequestHandler):

    def log_message(self, format, *args):
        return


class WSGIServerThread(threading.Thread):

    def __init__(self, app, host, port, log_length):
        super().__init__()
        self.app = app
        self.host = host
        self.port = port
        self.log_length = log_length
        self.server = None

    def run(self):
        log.info("[dev-server] Starting development Server...")
        self.server = make_server(
            self.host,
            self.port,
            self.app,
            server_class=QuietWSGIServer,
            handler_class=QuietHandler,
        )

        self.server.allow_reuse_address = True
        self.server.serve_forever()

    def stop(self):
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

    def run(self, *, log_length: int, src_path: str) -> None:
        if not self.thread:
            self.thread = WSGIServerThread(
                app=self.wsgi_app,
                host=self.host,
                port=self.port,
                log_length=log_length,
            )
            self.thread.start()

    def stop(self):
        if self.thread:
            self.thread.stop()
            self.thread.join()
            self.thread = None
