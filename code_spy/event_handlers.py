import time

from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent

from code_spy.tasks import BaseTask
from code_spy.logger import log


class FileEventHandler(FileSystemEventHandler):

    def __init__(self, *, tasks: list[BaseTask], log_length: int, observer):
        self.tasks = tasks
        self.last_time = 0
        self.log_length = log_length
        self.observer = observer
        super().__init__()

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if event.is_directory:
            return

        now = time.time()
        if now - self.last_time < 1:
            return
        self.last_time = now

        for task in self.tasks:
            task.stop()
            task.run(
                log_length=self.log_length,
                src_path=event.src_path,
            )
