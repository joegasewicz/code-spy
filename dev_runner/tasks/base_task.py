from abc import ABC, abstractmethod


class BaseTask(ABC):

    @abstractmethod
    def run(self) -> None: ...

    def stop(self) -> None:
        # Optional method
        pass
