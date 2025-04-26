from enum import Enum


class DocumentRecurringStatus(str, Enum):
    PAUSE = "PAUSE"
    RUNNING = "RUNNING"
    STOP = "STOP"
    WAITING = "WAITING"

    def __str__(self) -> str:
        return str(self.value)
