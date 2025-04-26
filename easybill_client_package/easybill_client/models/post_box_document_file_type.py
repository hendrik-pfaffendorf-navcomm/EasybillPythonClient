from enum import Enum


class PostBoxDocumentFileType(str, Enum):
    DEFAULT = "default"
    XRECHNUNG = "xrechnung"
    XRECHNUNG_XML = "xrechnung_xml"
    ZUGFERD1 = "zugferd1"
    ZUGFERD2 = "zugferd2"

    def __str__(self) -> str:
        return str(self.value)
