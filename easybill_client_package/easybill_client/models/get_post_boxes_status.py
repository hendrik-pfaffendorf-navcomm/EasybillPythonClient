from enum import Enum


class GetPostBoxesStatus(str, Enum):
    ERROR = "ERROR"
    OK = "OK"
    PREPARE = "PREPARE"
    PROCESSING = "PROCESSING"
    WAITING = "WAITING"

    def __str__(self) -> str:
        return str(self.value)
