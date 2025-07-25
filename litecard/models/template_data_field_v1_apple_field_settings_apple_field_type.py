from enum import Enum


class TemplateDataFieldV1AppleFieldSettingsAppleFieldType(str, Enum):
    AUXILIARY_FIELD = "AUXILIARY_FIELD"
    BACK_FIELD = "BACK_FIELD"
    HEADER_FIELD = "HEADER_FIELD"
    PRIMARY_FIELD = "PRIMARY_FIELD"
    SECONDARY_FIELD = "SECONDARY_FIELD"

    def __str__(self) -> str:
        return str(self.value)
