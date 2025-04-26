from enum import Enum


class DocumentRecurringSendAs(str, Enum):
    EMAIL = "EMAIL"
    FAX = "FAX"
    POST = "POST"

    def __str__(self) -> str:
        return str(self.value)
