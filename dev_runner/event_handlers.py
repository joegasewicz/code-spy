import time

from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent

from dev_runner.tasks import BaseTask


class FileEventHandler(FileSystemEventHandler):

    def __init__(self, *, tasks: list[BaseTask], observer):
        self.tasks = tasks
        self.last_time = 0
        self.observer = observer
        super()

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if event.is_directory:
            return

        now = time.time()
        if now - self.last_time < 1:
            return
        self.last_time = now

        if not event.is_directory:
            for task in self.tasks:
                task.stop()
                task.run()
