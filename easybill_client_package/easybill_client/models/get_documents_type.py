from enum import Enum


class GetDocumentsType(str, Enum):
    CHARGE = "CHARGE"
    CHARGE_CONFIRM = "CHARGE_CONFIRM"
    CREDIT = "CREDIT"
    DELIVERY = "DELIVERY"
    DUNNING = "DUNNING"
    INVOICE = "INVOICE"
    LETTER = "LETTER"
    OFFER = "OFFER"
    ORDER = "ORDER"
    PDF = "PDF"
    PROFORMA_INVOICE = "PROFORMA_INVOICE"
    RECURRING = "RECURRING"
    REMINDER = "REMINDER"
    STORNO = "STORNO"
    STORNO_CREDIT = "STORNO_CREDIT"
    STORNO_PROFORMA_INVOICE = "STORNO_PROFORMA_INVOICE"

    def __str__(self) -> str:
        return str(self.value)
