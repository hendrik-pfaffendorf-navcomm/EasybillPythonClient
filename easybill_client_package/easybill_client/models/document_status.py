from enum import Enum


class DocumentStatus(str, Enum):
    ACCEPT = "ACCEPT"
    CANCEL = "CANCEL"
    DONE = "DONE"
    DROPSHIPPING = "DROPSHIPPING"

    def __str__(self) -> str:
        return str(self.value)
