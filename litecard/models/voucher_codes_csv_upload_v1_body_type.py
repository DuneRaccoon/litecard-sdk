from enum import Enum


class VoucherCodesCSVUploadV1BodyType(str, Enum):
    EMAIL = "EMAIL"
    EMAIL_MEMBER = "EMAIL_MEMBER"
    VOUCHER = "VOUCHER"

    def __str__(self) -> str:
        return str(self.value)
