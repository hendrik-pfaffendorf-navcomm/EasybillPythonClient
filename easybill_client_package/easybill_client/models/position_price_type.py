from enum import Enum


class PositionPriceType(str, Enum):
    BRUTTO = "BRUTTO"
    NETTO = "NETTO"

    def __str__(self) -> str:
        return str(self.value)
