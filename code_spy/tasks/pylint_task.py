from pylint import lint



from code_spy.tasks.base_task import BaseTask
from code_spy.logger import log

PYLINT_SYSTEM_EXIT = 16


class PylintTask(BaseTask):

    def __init__(self, *, path: str, rcfile: str = None, args: str = None):
        self.path = path
        self.rcfile = rcfile
        self.args = args

    def run(self) -> None:
        args = [self.path]
        if self.rcfile:
            args.append("--rcfile")
            args.append(self.rcfile)
        if self.args:
            args.append(self.args)
        log.info("[pylint] Starting linting...")
        try:
            lint.Run(args)
        except SystemExit as e:
            if e.code == PYLINT_SYSTEM_EXIT:
                pass

    def stop(self) -> None:
        pass
