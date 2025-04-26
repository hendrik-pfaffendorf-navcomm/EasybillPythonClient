from enum import Enum


class DocumentRecurringTargetType(str, Enum):
    CREDIT = "CREDIT"
    INVOICE = "INVOICE"
    OFFER = "OFFER"
    ORDER = "ORDER"

    def __str__(self) -> str:
        return str(self.value)
