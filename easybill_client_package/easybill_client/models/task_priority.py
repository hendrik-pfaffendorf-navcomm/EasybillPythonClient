from enum import Enum


class TaskPriority(str, Enum):
    HIGH = "HIGH"
    LOW = "LOW"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
