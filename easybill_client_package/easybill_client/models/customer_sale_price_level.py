from enum import Enum


class CustomerSalePriceLevel(str, Enum):
    SALEPRICE10 = "SALEPRICE10"
    SALEPRICE2 = "SALEPRICE2"
    SALEPRICE3 = "SALEPRICE3"
    SALEPRICE4 = "SALEPRICE4"
    SALEPRICE5 = "SALEPRICE5"
    SALEPRICE6 = "SALEPRICE6"
    SALEPRICE7 = "SALEPRICE7"
    SALEPRICE8 = "SALEPRICE8"
    SALEPRICE9 = "SALEPRICE9"

    def __str__(self) -> str:
        return str(self.value)
