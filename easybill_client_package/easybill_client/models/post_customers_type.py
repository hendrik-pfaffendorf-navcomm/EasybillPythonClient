from enum import Enum


class PostCustomersType(str, Enum):
    CUSTOMER = "CUSTOMER"
    CUSTOMERSUPPLIER = "CUSTOMER,SUPPLIER"
    SUPPLIER = "SUPPLIER"

    def __str__(self) -> str:
        return str(self.value)
