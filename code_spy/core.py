from watchdog.observers import Observer

from code_spy.logger import log, preamble_log
from code_spy.tasks import BaseTask
from code_spy.event_handlers import FileEventHandler


class CodeSpy:

    def __init__(
            self,
            *,
            watch_path: str = ".",
            tasks: list[BaseTask],
            log_length: int = 100,
            interval: int = 1,
            ignore_dirs: list[str] = None,
    ):
        self.watch_path = watch_path
        self.tasks = tasks
        self.log_length = log_length
        self.interval = interval
        self.ignore_dirs = ignore_dirs or []

        self.observer = Observer()
        self.file_handler = FileEventHandler(
            tasks=self.tasks,
            log_length=self.log_length,
            observer=self.observer,
            interval=self.interval,
            ignore_dirs=self.ignore_dirs,
        )
        preamble_log()
        self.run()

    def run(self):
        for task in self.tasks:
            # Pass an empty string to src_path as no operation has taken place yet.
            task.run(log_length=self.log_length, src_path="")

    def watch(self):
        self.observer.schedule(self.file_handler, self.watch_path, recursive=True)
        self.observer.start()
        self.observer.join()
