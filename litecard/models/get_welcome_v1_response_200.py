from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.welcome_details_response import WelcomeDetailsResponse


T = TypeVar("T", bound="GetWelcomeV1Response200")


@_attrs_define
class GetWelcomeV1Response200:
    """
    Attributes:
        body (Union[Unset, WelcomeDetailsResponse]): Download Urls for welcome page
    """

    body: Union[Unset, "WelcomeDetailsResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.body, Unset):
            body = self.body.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.welcome_details_response import WelcomeDetailsResponse

        d = dict(src_dict)
        _body = d.pop("body", UNSET)
        body: Union[Unset, WelcomeDetailsResponse]
        if isinstance(_body, Unset):
            body = UNSET
        else:
            body = WelcomeDetailsResponse.from_dict(_body)

        get_welcome_v1_response_200 = cls(
            body=body,
        )

        get_welcome_v1_response_200.additional_properties = d
        return get_welcome_v1_response_200

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
