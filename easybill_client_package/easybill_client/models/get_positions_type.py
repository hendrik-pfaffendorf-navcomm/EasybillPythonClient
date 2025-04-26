from enum import Enum


class GetPositionsType(str, Enum):
    PRODUCT = "PRODUCT"
    SERVICE = "SERVICE"
    TEXT = "TEXT"

    def __str__(self) -> str:
        return str(self.value)
