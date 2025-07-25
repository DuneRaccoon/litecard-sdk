from enum import Enum


class TemplateDataFieldV1GoogleFieldSettingsFieldType(str, Enum):
    TEXT = "TEXT"
    TEXT_AND_NOTIFY = "TEXT_AND_NOTIFY"

    def __str__(self) -> str:
        return str(self.value)
