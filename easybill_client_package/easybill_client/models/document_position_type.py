from enum import Enum


class DocumentPositionType(str, Enum):
    POSITION = "POSITION"
    POSITION_NOCALC = "POSITION_NOCALC"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
