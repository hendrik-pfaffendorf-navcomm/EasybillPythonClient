from enum import Enum


class PostBoxRequestDocumentFileType(str, Enum):
    DEFAULT = "default"
    XRECHNUNG = "xrechnung"
    XRECHNUNG2_2_XML = "xrechnung2_2_xml"
    XRECHNUNG3_0_XML = "xrechnung3_0_xml"
    XRECHNUNG_XML = "xrechnung_xml"
    ZUGFERD1 = "zugferd1"
    ZUGFERD2 = "zugferd2"

    def __str__(self) -> str:
        return str(self.value)
