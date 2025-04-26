from enum import Enum


class SEPAPaymentSequenceType(str, Enum):
    FNAL = "FNAL"
    FRST = "FRST"
    OOFF = "OOFF"
    RCUR = "RCUR"

    def __str__(self) -> str:
        return str(self.value)
