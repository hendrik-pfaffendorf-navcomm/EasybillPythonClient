from enum import Enum


class PositionType(str, Enum):
    PRODUCT = "PRODUCT"
    SERVICE = "SERVICE"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
