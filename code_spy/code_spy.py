import time

from watchdog.observers import Observer


from code_spy.logger import log
from code_spy.tasks import BaseTask
from code_spy.event_handlers import FileEventHandler


class CodeSpy:

    def __init__(self, *, path: str, tasks: list[BaseTask]):
        self.path = path
        self.tasks = tasks
        self.observer = Observer()
        self.file_handler = FileEventHandler(tasks=self.tasks, observer=self.observer)
        log.info("Starting dev-runner..")

    def run(self):
        for task in self.tasks:
            task.run()

    def watch(self):
        self.run()

        self.observer.schedule(self.file_handler, self.path, recursive=True)
        self.observer.start()

        self.observer.join()
