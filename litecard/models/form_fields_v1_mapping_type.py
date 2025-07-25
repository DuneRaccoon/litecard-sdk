from enum import Enum


class FormFieldsV1MappingType(str, Enum):
    CARD = "CARD"
    CARD_OWNER = "CARD_OWNER"
    CARD_OWNER_AND_CARD = "CARD_OWNER_AND_CARD"

    def __str__(self) -> str:
        return str(self.value)
