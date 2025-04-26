from enum import Enum


class CustomerTaxOptions(str, Enum):
    AL = "AL"
    IG = "IG"
    NSTB = "nStb"
    NSTBIM = "nStbIm"
    NSTBNONEUSTID = "nStbNoneUstID"
    NSTBUSTID = "nStbUstID"
    NULL = "NULL"
    REVC = "revc"
    SSTFR = "sStfr"

    def __str__(self) -> str:
        return str(self.value)
