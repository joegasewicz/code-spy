import textwrap
from pylint import lint
from pylint.message import Message
from pylint.reporters import BaseReporter, ReportsHandlerMixIn
from pylint.reporters.ureports.nodes import Section
from pylint.utils import LinterStats

from code_spy.tasks.base_task import BaseTask
from code_spy.logger import log

PYLINT_SYSTEM_EXIT = 16


class SilentReporter(BaseReporter, ReportsHandlerMixIn):

    final_score = None

    def handle_message(self, msg: Message) -> None:
        if msg:
            log.error(f"[pylint] ({msg.msg_id}) {msg.msg} {msg.path}")
        self.messages.append(msg)

    def display_messages(self, layout: Section | None) -> None:
        pass

    def _display(self, layout: Section) -> None:
        pass

    def on_close(
        self,
        stats: LinterStats,
        previous_stats: LinterStats | None,
    ) -> None:
        score = stats.global_note
        previous_score = previous_stats.global_note
        if len(self.messages) == 0:
            score = score if score != 0 else previous_score # TODO Issue - #25
            log.info(f"[pylint] Your code has been rated at {score:.2f}/10")

class PylintTask(BaseTask):

    def __init__(self, *, path: str, rcfile: str = None, args: str = None):
        self.path = path
        self.rcfile = rcfile
        self.args = args

    def run(self, *, log_length: int, src_path: str) -> None:
        args = [self.path]
        if self.rcfile:
            args.append("--rcfile")
            args.append(self.rcfile)
        if self.args:
            args.append(self.args)

        try:
            result = lint.Run(args, reporter=SilentReporter())
        except SystemExit as e:
            if e.code == PYLINT_SYSTEM_EXIT:
                pass

    def stop(self) -> None:
        pass
