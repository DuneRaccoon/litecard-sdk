from enum import Enum


class TemplateBarcodeV1Type(str, Enum):
    AZTEC = "AZTEC"
    CODE_128 = "CODE_128"
    NOT_USED = "NOT_USED"
    PDF_417 = "PDF_417"
    QR_CODE = "QR_CODE"

    def __str__(self) -> str:
        return str(self.value)
