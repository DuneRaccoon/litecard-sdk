from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_config import TableConfig


T = TypeVar("T", bound="CreateSubBusinessRequestBody")


@_attrs_define
class CreateSubBusinessRequestBody:
    """
    Attributes:
        business_name (Union[Unset, str]): Business name Example: Cryo gym.
        email (Union[Unset, str]): Business email Example: Ankus Fang.
        password (Union[Unset, str]): Business password Example: password.
        app_urls (Union[Unset, list[str]]): App urls
        country (Union[Unset, str]): Business country Example: Australia.
        post_code (Union[Unset, str]): Business postcode Example: CryoGym.
        phone (Union[Unset, str]): Business phone Example: Ankus Fang.
        state (Union[Unset, str]): Business state Example: VIC.
        logo_image (Union[None, Unset, str]): Business logo image file Example: base64 encoded image.
        table_config (Union[Unset, TableConfig]):
    """

    business_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    app_urls: Union[Unset, list[str]] = UNSET
    country: Union[Unset, str] = UNSET
    post_code: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    logo_image: Union[None, Unset, str] = UNSET
    table_config: Union[Unset, "TableConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_name = self.business_name

        email = self.email

        password = self.password

        app_urls: Union[Unset, list[str]] = UNSET
        if not isinstance(self.app_urls, Unset):
            app_urls = self.app_urls

        country = self.country

        post_code = self.post_code

        phone = self.phone

        state = self.state

        logo_image: Union[None, Unset, str]
        if isinstance(self.logo_image, Unset):
            logo_image = UNSET
        else:
            logo_image = self.logo_image

        table_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.table_config, Unset):
            table_config = self.table_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if email is not UNSET:
            field_dict["email"] = email
        if password is not UNSET:
            field_dict["password"] = password
        if app_urls is not UNSET:
            field_dict["appUrls"] = app_urls
        if country is not UNSET:
            field_dict["country"] = country
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if phone is not UNSET:
            field_dict["phone"] = phone
        if state is not UNSET:
            field_dict["state"] = state
        if logo_image is not UNSET:
            field_dict["logoImage"] = logo_image
        if table_config is not UNSET:
            field_dict["tableConfig"] = table_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_config import TableConfig

        d = dict(src_dict)
        business_name = d.pop("businessName", UNSET)

        email = d.pop("email", UNSET)

        password = d.pop("password", UNSET)

        app_urls = cast(list[str], d.pop("appUrls", UNSET))

        country = d.pop("country", UNSET)

        post_code = d.pop("postCode", UNSET)

        phone = d.pop("phone", UNSET)

        state = d.pop("state", UNSET)

        def _parse_logo_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_image = _parse_logo_image(d.pop("logoImage", UNSET))

        _table_config = d.pop("tableConfig", UNSET)
        table_config: Union[Unset, TableConfig]
        if isinstance(_table_config, Unset):
            table_config = UNSET
        else:
            table_config = TableConfig.from_dict(_table_config)

        create_sub_business_request_body = cls(
            business_name=business_name,
            email=email,
            password=password,
            app_urls=app_urls,
            country=country,
            post_code=post_code,
            phone=phone,
            state=state,
            logo_image=logo_image,
            table_config=table_config,
        )

        create_sub_business_request_body.additional_properties = d
        return create_sub_business_request_body

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
