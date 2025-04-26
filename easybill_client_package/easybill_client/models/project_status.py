from enum import Enum


class ProjectStatus(str, Enum):
    CANCEL = "CANCEL"
    DONE = "DONE"
    OPEN = "OPEN"

    def __str__(self) -> str:
        return str(self.value)
