from enum import Enum


class DocumentRecurringSepaSequenceType(str, Enum):
    FNAL = "FNAL"
    FRST = "FRST"
    OOFF = "OOFF"
    RCUR = "RCUR"

    def __str__(self) -> str:
        return str(self.value)
