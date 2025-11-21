from pathlib import Path

from black import (
    format_file_in_place,
    FileMode,
    WriteBack,
    NothingChanged,
)
from black.linegen import CannotSplit, CannotTransform


from code_spy.tasks.base_task import BaseTask
from code_spy.logger import log


BLACK_HAPPY_LOG = "All done! ✨ 🍰 ✨ 1 file reformatted."
BLACK_NO_FILES_ERROR_LOG = "No Python files are present to be formatted. Nothing to do 😴"
BLACK_ERROR_LOG = "Oh no! 💥 💔 💥"


class BlackTask(BaseTask):

    def __init__(self, *, path: str):
        self.path = path
        self.root_path = Path(self.path)

    def run(self, *, log_length: int, src_path: str) -> None:
        try:
            if src_path:
                file_path = Path(src_path)
                format_file_in_place(
                    file_path,
                    fast=False,
                    mode=FileMode(),
                    write_back=WriteBack.YES,
                )
                root_path = Path.cwd()
                rel_file_path = file_path.relative_to(root_path)
                log.info(f"[black] {BLACK_HAPPY_LOG} {rel_file_path}")
        except (NothingChanged, CannotSplit, CannotTransform) as err:
            log.error(f"[black] {BLACK_ERROR_LOG} {err}")
        except (ValueError, AssertionError) as err:
            log.error(f"[black] {BLACK_ERROR_LOG} {err}")
        except Exception as err:
            # If we arrive here then something terrible has happened
            log.error(f"[black] Error: {err}", exc_info=err)


    def stop(self) -> None:
        pass
