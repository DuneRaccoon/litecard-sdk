from enum import Enum


class TemplateDataFieldV1FormFieldSettingsDataType(str, Enum):
    DATE = "date"
    DATETIME = "dateTime"
    IMAGE = "image"
    NATIONALITY = "nationality"
    NUMBER = "number"
    PHONE = "phone"
    RADIO = "radio"
    SELECT = "select"
    TEXT = "text"
    TEXTAREA = "textArea"

    def __str__(self) -> str:
        return str(self.value)
