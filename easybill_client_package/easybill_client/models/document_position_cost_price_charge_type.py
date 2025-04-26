from enum import Enum


class DocumentPositionCostPriceChargeType(str, Enum):
    AMOUNT = "AMOUNT"
    PERCENT = "PERCENT"

    def __str__(self) -> str:
        return str(self.value)
