from enum import Enum


class TaskStatus(str, Enum):
    CANCEL = "CANCEL"
    DONE = "DONE"
    PROCESSING = "PROCESSING"
    WAITING = "WAITING"

    def __str__(self) -> str:
        return str(self.value)
