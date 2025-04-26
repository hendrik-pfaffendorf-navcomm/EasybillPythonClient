from enum import Enum


class PostDocumentsIdSendTypeType(str, Enum):
    EMAIL = "email"
    FAX = "fax"
    POST = "post"

    def __str__(self) -> str:
        return str(self.value)
