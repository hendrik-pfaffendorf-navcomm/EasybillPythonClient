from enum import Enum


class CustomerDocumentPdfType(str, Enum):
    DEFAULT = "default"
    XRECHNUNG2_1_XML = "xrechnung2_1_xml"
    XRECHNUNG2_2_XML = "xrechnung2_2_xml"
    XRECHNUNG2_3_XML = "xrechnung2_3_xml"
    XRECHNUNG3_0_XML = "xrechnung3_0_xml"
    ZUGFERD1 = "zugferd1"
    ZUGFERD2_2 = "zugferd2_2"

    def __str__(self) -> str:
        return str(self.value)
