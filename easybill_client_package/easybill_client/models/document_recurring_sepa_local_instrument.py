from enum import Enum


class DocumentRecurringSepaLocalInstrument(str, Enum):
    B2B = "B2B"
    COR1 = "COR1"
    CORE = "CORE"

    def __str__(self) -> str:
        return str(self.value)
