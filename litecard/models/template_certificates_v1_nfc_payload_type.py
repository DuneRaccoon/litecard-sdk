from enum import Enum


class TemplateCertificatesV1NfcPayloadType(str, Enum):
    BARCODE_VALUE = "BARCODE_VALUE"

    def __str__(self) -> str:
        return str(self.value)
