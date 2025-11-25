import time
from pathlib import Path

from watchdog.events import FileSystemEventHandler, DirModifiedEvent, FileModifiedEvent

from code_spy.tasks import BaseTask
from code_spy.logger import log


class FileEventHandler(FileSystemEventHandler):

    def __init__(
        self,
        *,
        tasks: list[BaseTask],
        log_length: int,
        observer = None,
        interval: int = 1,
        ignore_dirs: list[str],
    ):
        self.tasks = tasks
        self.last_time = 0
        self.log_length = log_length
        self.observer = observer
        self.interval = interval
        _ignore_list = [
            ".mypy_cache",
            "__pycache__ ",
            ".pytest_cache",
            "pylint.d",
            ".DS_Store",
            ".idea",
            ".vscode",
            ".git",
        ]
        self.ignore_dirs = [*ignore_dirs, *_ignore_list]
        super().__init__()

    def on_modified(self, event: DirModifiedEvent | FileModifiedEvent) -> None:
        if event.is_directory:
            return
        if self._skip_event_if_in_ignore_dirs(event=event):
            return
        now = time.time()
        if now - self.last_time < self.interval:
            return
        self.last_time = now

        for task in self.tasks:
            task.stop()
            task.run(
                log_length=self.log_length,
                src_path=event.src_path,
            )

    def _skip_event_if_in_ignore_dirs(self, *, event) -> bool:
        src_parts = Path(event.src_path).parts
        for ignore in self.ignore_dirs:
            if ignore in src_parts:
                return True
        return False