from enum import Enum


class DocumentRecurringPaidDateOption(str, Enum):
    CREATED_DATE = "created_date"
    DUE_DATE = "due_date"
    NEXT_VALID_DATE = "next_valid_date"

    def __str__(self) -> str:
        return str(self.value)
