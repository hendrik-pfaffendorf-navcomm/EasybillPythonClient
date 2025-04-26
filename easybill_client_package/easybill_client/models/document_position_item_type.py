from enum import Enum


class DocumentPositionItemType(str, Enum):
    PRODUCT = "PRODUCT"
    SERVICE = "SERVICE"
    UNDEFINED = "UNDEFINED"

    def __str__(self) -> str:
        return str(self.value)
