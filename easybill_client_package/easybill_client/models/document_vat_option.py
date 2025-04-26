from enum import Enum


class DocumentVatOption(str, Enum):
    AL = "AL"
    IG = "IG"
    NSTB = "nStb"
    NSTBIM = "nStbIm"
    NSTBNONEUSTID = "nStbNoneUstID"
    NSTBUSTID = "nStbUstID"
    NULL = "NULL"
    REVC = "revc"
    SMALLBUSINESS = "smallBusiness"
    SSTFR = "sStfr"

    def __str__(self) -> str:
        return str(self.value)
