from enum import Enum


class FormFieldsV1RulesItem(str, Enum):
    EMAIL = "email"
    INTEGER = "integer"
    PHONE = "phone"
    REQUIRED = "required"

    def __str__(self) -> str:
        return str(self.value)
