from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ui_page_schema import UIPageSchema


T = TypeVar("T", bound="UIConfig")


@_attrs_define
class UIConfig:
    """Configuration for the UI

    Attributes:
        signup_page (Union[Unset, UIPageSchema]):
    """

    signup_page: Union[Unset, "UIPageSchema"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        signup_page: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.signup_page, Unset):
            signup_page = self.signup_page.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if signup_page is not UNSET:
            field_dict["signupPage"] = signup_page

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_page_schema import UIPageSchema

        d = dict(src_dict)
        _signup_page = d.pop("signupPage", UNSET)
        signup_page: Union[Unset, UIPageSchema]
        if isinstance(_signup_page, Unset):
            signup_page = UNSET
        else:
            signup_page = UIPageSchema.from_dict(_signup_page)

        ui_config = cls(
            signup_page=signup_page,
        )

        ui_config.additional_properties = d
        return ui_config

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
