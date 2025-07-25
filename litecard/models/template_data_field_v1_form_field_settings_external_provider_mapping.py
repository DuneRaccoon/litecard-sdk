from enum import Enum


class TemplateDataFieldV1FormFieldSettingsExternalProviderMapping(str, Enum):
    CUSTOMER_ID = "CUSTOMER_ID"
    LOYALTY_MEMBER_ID = "LOYALTY_MEMBER_ID"
    LOYALTY_POINTS = "LOYALTY_POINTS"
    VALID_EMAIL = "VALID_EMAIL"
    VALID_EMAIL_MAPPING_CODE = "VALID_EMAIL_MAPPING_CODE"
    VOUCHER_CODE = "VOUCHER_CODE"

    def __str__(self) -> str:
        return str(self.value)
