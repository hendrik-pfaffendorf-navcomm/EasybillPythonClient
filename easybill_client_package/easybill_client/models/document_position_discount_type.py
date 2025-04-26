from enum import Enum


class DocumentPositionDiscountType(str, Enum):
    AMOUNT = "AMOUNT"
    FIX = "FIX"
    PERCENT = "PERCENT"
    QUANTITY = "QUANTITY"

    def __str__(self) -> str:
        return str(self.value)
