from abc import ABC, abstractmethod


class BaseTask(ABC):

    @abstractmethod
    def run(self, *, log_length: int) -> None: ...

    @abstractmethod
    def stop(self) -> None: ...
