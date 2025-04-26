from enum import Enum


class WebHookContentType(str, Enum):
    FORM = "form"
    JSON = "json"

    def __str__(self) -> str:
        return str(self.value)
