from enum import Enum


class FormFieldsType(str, Enum):
    NUMBER = "number"
    PHONE = "phone"
    RADIO = "radio"
    SELECT = "select"
    TEXT = "text"
    TEXTAREA = "textArea"

    def __str__(self) -> str:
        return str(self.value)
