from enum import Enum


class PositionStockLimitNotifyFrequency(str, Enum):
    ALWAYS = "ALWAYS"
    ONCE = "ONCE"

    def __str__(self) -> str:
        return str(self.value)
