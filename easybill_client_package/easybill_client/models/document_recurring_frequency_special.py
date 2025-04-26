from enum import Enum


class DocumentRecurringFrequencySpecial(str, Enum):
    LASTDAYOFMONTH = "LASTDAYOFMONTH"

    def __str__(self) -> str:
        return str(self.value)
