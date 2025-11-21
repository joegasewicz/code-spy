from watchdog.observers import Observer

from code_spy.logger import log, preamble_log
from code_spy.tasks import BaseTask
from code_spy.event_handlers import FileEventHandler


class CodeSpy:

    def __init__(
            self,
            *,
            path: str,
            tasks: list[BaseTask],
            log_length: int = 100,
    ):
        self.path = path
        self.tasks = tasks
        self.log_length = log_length

        self.observer = Observer()
        self.file_handler = FileEventHandler(
            tasks=self.tasks,
            log_length=self.log_length,
            observer=self.observer,
        )
        preamble_log()
        self.run()

    def run(self):
        for task in self.tasks:
            # Pass an empty string to src_path as no operation has taken place yet.
            task.run(log_length=self.log_length, src_path="")

    def watch(self):
        self.observer.schedule(self.file_handler, self.path, recursive=True)
        self.observer.start()
        self.observer.join()
