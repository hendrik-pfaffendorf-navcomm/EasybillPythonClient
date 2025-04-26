from enum import Enum


class PositionStock(str, Enum):
    NO = "NO"
    YES = "YES"

    def __str__(self) -> str:
        return str(self.value)
