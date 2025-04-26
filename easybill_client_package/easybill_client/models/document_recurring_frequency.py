from enum import Enum


class DocumentRecurringFrequency(str, Enum):
    DAILY = "DAILY"
    MONTHLY = "MONTHLY"
    WEEKLY = "WEEKLY"
    YEARLY = "YEARLY"

    def __str__(self) -> str:
        return str(self.value)
