from enum import Enum


class PutCustomersIdType(str, Enum):
    CUSTOMER = "CUSTOMER"
    CUSTOMERSUPPLIER = "CUSTOMER,SUPPLIER"
    SUPPLIER = "SUPPLIER"

    def __str__(self) -> str:
        return str(self.value)
