from enum import Enum


class PostDocumentsIdTypeType(str, Enum):
    CHARGE = "CHARGE"
    CHARGE_CONFIRM = "CHARGE_CONFIRM"
    CREDIT = "CREDIT"
    DELIVERY = "DELIVERY"
    DUNNING = "DUNNING"
    INVOICE = "INVOICE"
    ORDER = "ORDER"
    REMINDER = "REMINDER"

    def __str__(self) -> str:
        return str(self.value)
