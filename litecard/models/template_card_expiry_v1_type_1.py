from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.template_card_expiry_v1_type_1_expiry_type import TemplateCardExpiryV1Type1ExpiryType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TemplateCardExpiryV1Type1")


@_attrs_define
class TemplateCardExpiryV1Type1:
    """
    Attributes:
        expiry_type (Union[Unset, TemplateCardExpiryV1Type1ExpiryType]): Type of expiry, either NEVER, FIXED_DATE,
            FROM_ACTIVATION or FIXED_SCANS Example: FIXED_DATE.
        start_date (Union[Unset, str]): ISO 8601 date time that the card becomes active in the users digital wallet. For
            Apple cards, the card is still active however it will show up on the top of the stack and Google cards there is
            no effect unless they are grouped Example: 2022-11-24T20:40:07Z.
        end_date (Union[Unset, str]): ISO 8601 date time that the card expires in the users digital wallet Example:
            2022-11-24T20:40:07Z.
    """

    expiry_type: Union[Unset, TemplateCardExpiryV1Type1ExpiryType] = UNSET
    start_date: Union[Unset, str] = UNSET
    end_date: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        expiry_type: Union[Unset, str] = UNSET
        if not isinstance(self.expiry_type, Unset):
            expiry_type = self.expiry_type.value

        start_date = self.start_date

        end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if expiry_type is not UNSET:
            field_dict["expiryType"] = expiry_type
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _expiry_type = d.pop("expiryType", UNSET)
        expiry_type: Union[Unset, TemplateCardExpiryV1Type1ExpiryType]
        if isinstance(_expiry_type, Unset):
            expiry_type = UNSET
        else:
            expiry_type = TemplateCardExpiryV1Type1ExpiryType(_expiry_type)

        start_date = d.pop("startDate", UNSET)

        end_date = d.pop("endDate", UNSET)

        template_card_expiry_v1_type_1 = cls(
            expiry_type=expiry_type,
            start_date=start_date,
            end_date=end_date,
        )

        template_card_expiry_v1_type_1.additional_properties = d
        return template_card_expiry_v1_type_1

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
