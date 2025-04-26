from enum import Enum


class LoginLoginType(str, Enum):
    ADMIN = "ADMIN"
    ASSISTANT = "ASSISTANT"

    def __str__(self) -> str:
        return str(self.value)
