from enum import Enum


class CustomerSepaAgreement(str, Enum):
    BASIC = "BASIC"
    COMPANY = "COMPANY"
    COR1 = "COR1"
    NULL = "NULL"

    def __str__(self) -> str:
        return str(self.value)
