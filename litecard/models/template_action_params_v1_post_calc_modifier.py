from enum import Enum


class TemplateActionParamsV1PostCalcModifier(str, Enum):
    DISCOUNT = "DISCOUNT"
    PERCENTAGE = "PERCENTAGE"

    def __str__(self) -> str:
        return str(self.value)
