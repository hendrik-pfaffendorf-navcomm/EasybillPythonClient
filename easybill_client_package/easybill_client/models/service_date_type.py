from enum import Enum


class ServiceDateType(str, Enum):
    DEFAULT = "DEFAULT"
    DELIVERY = "DELIVERY"
    SERVICE = "SERVICE"

    def __str__(self) -> str:
        return str(self.value)
