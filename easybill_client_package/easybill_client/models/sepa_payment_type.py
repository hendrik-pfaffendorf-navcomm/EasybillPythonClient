from enum import Enum


class SEPAPaymentType(str, Enum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"

    def __str__(self) -> str:
        return str(self.value)
