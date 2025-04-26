from enum import Enum


class TaskCategory(str, Enum):
    CALL = "CALL"
    CUSTOM = "CUSTOM"
    EMAIL = "EMAIL"
    FAX = "FAX"
    LUNCH = "LUNCH"
    MEETING = "MEETING"
    TRAVEL = "TRAVEL"

    def __str__(self) -> str:
        return str(self.value)
