from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.social_media import SocialMedia


T = TypeVar("T", bound="BusinessCardOptions")


@_attrs_define
class BusinessCardOptions:
    """
    Attributes:
        first_name (Union[Unset, str]): First Name Example: John.
        last_name (Union[Unset, str]): Last Name Example: Doe.
        middle_name (Union[Unset, str]): Middle Name Example: Sam.
        email (Union[Unset, str]): Email field for email address Example: john@litecard.com.au.
        work_phone (Union[Unset, str]): Work phone number Example: +61400000000.
        home_phone (Union[Unset, str]): Home phone number Example: +61400000000.
        company (Union[Unset, str]): Company of Employment Example: Litecard.
        title (Union[Unset, str]): Title of position at Company Example: Developer.
        social (Union[Unset, list['SocialMedia']]):
    """

    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    work_phone: Union[Unset, str] = UNSET
    home_phone: Union[Unset, str] = UNSET
    company: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    social: Union[Unset, list["SocialMedia"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        middle_name = self.middle_name

        email = self.email

        work_phone = self.work_phone

        home_phone = self.home_phone

        company = self.company

        title = self.title

        social: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.social, Unset):
            social = []
            for social_item_data in self.social:
                social_item = social_item_data.to_dict()
                social.append(social_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if email is not UNSET:
            field_dict["email"] = email
        if work_phone is not UNSET:
            field_dict["workPhone"] = work_phone
        if home_phone is not UNSET:
            field_dict["homePhone"] = home_phone
        if company is not UNSET:
            field_dict["company"] = company
        if title is not UNSET:
            field_dict["title"] = title
        if social is not UNSET:
            field_dict["social"] = social

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.social_media import SocialMedia

        d = dict(src_dict)
        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        email = d.pop("email", UNSET)

        work_phone = d.pop("workPhone", UNSET)

        home_phone = d.pop("homePhone", UNSET)

        company = d.pop("company", UNSET)

        title = d.pop("title", UNSET)

        social = []
        _social = d.pop("social", UNSET)
        for social_item_data in _social or []:
            social_item = SocialMedia.from_dict(social_item_data)

            social.append(social_item)

        business_card_options = cls(
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            email=email,
            work_phone=work_phone,
            home_phone=home_phone,
            company=company,
            title=title,
            social=social,
        )

        business_card_options.additional_properties = d
        return business_card_options

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
