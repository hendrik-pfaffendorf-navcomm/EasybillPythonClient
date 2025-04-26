from enum import Enum


class DocumentAnonymizeStatus(str, Enum):
    ANONYMIZED = "ANONYMIZED"
    NOT_ANONYMIZED = "NOT_ANONYMIZED"

    def __str__(self) -> str:
        return str(self.value)
