import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent
from mypy import api

from dev_runner.logger import log


class FileHandler(FileSystemEventHandler):

    def __init__(self, *, path: str, file: str):
        self.path = path
        self.file = file
        super()

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if not event.is_directory:
            result = api.run([
                "--strict",
                self.file,
            ])

            log.info(f"stdout: {result[0]}")
            log.info(f"stderr: {result[1]}")
            log.info(f"exit status: {result[2]}")


class DevRunner:

    def __init__(self, *, path: str, file: str):
        self.path = path
        self.file = file
        self.file_handler = FileHandler(path=self.path, file=self.file)
        log.info("Starting dev-runner..")

    def watch(self):
        observer = Observer()
        observer.schedule(self.file_handler, self.path, recursive=True)
        observer.start()
        observer.join()
