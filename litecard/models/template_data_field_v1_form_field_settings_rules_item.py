from enum import Enum


class TemplateDataFieldV1FormFieldSettingsRulesItem(str, Enum):
    EMAIL = "email"
    INTEGER = "integer"
    PHONE = "phone"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
