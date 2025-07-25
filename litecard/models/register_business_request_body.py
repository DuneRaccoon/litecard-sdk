from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.table_config import TableConfig


T = TypeVar("T", bound="RegisterBusinessRequestBody")


@_attrs_define
class RegisterBusinessRequestBody:
    """
    Attributes:
        business_name (str): Name of the business Example: Litecard.
        token (str): Token for the business Example: token.
        logo_image (Union[None, str]): Business logo image file Example: base64 encoded image.
        email (str): Contact email for the business Example: test@ww.com.
        password (str): Password for the business Example: password.
        dashboard_access (list[str]): Access to the dashboard
        app_urls (list[str]): Urls of apps allowed
        is_master_business (Union[Unset, bool]): Is the business a master business Example: True.
        table_config (Union[Unset, TableConfig]):
    """

    business_name: str
    token: str
    logo_image: Union[None, str]
    email: str
    password: str
    dashboard_access: list[str]
    app_urls: list[str]
    is_master_business: Union[Unset, bool] = UNSET
    table_config: Union[Unset, "TableConfig"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_name = self.business_name

        token = self.token

        logo_image: Union[None, str]
        logo_image = self.logo_image

        email = self.email

        password = self.password

        dashboard_access = self.dashboard_access

        app_urls = self.app_urls

        is_master_business = self.is_master_business

        table_config: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.table_config, Unset):
            table_config = self.table_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "businessName": business_name,
                "token": token,
                "logoImage": logo_image,
                "email": email,
                "password": password,
                "dashboardAccess": dashboard_access,
                "appUrls": app_urls,
            }
        )
        if is_master_business is not UNSET:
            field_dict["isMasterBusiness"] = is_master_business
        if table_config is not UNSET:
            field_dict["tableConfig"] = table_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_config import TableConfig

        d = dict(src_dict)
        business_name = d.pop("businessName")

        token = d.pop("token")

        def _parse_logo_image(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        logo_image = _parse_logo_image(d.pop("logoImage"))

        email = d.pop("email")

        password = d.pop("password")

        dashboard_access = cast(list[str], d.pop("dashboardAccess"))

        app_urls = cast(list[str], d.pop("appUrls"))

        is_master_business = d.pop("isMasterBusiness", UNSET)

        _table_config = d.pop("tableConfig", UNSET)
        table_config: Union[Unset, TableConfig]
        if isinstance(_table_config, Unset):
            table_config = UNSET
        else:
            table_config = TableConfig.from_dict(_table_config)

        register_business_request_body = cls(
            business_name=business_name,
            token=token,
            logo_image=logo_image,
            email=email,
            password=password,
            dashboard_access=dashboard_access,
            app_urls=app_urls,
            is_master_business=is_master_business,
            table_config=table_config,
        )

        register_business_request_body.additional_properties = d
        return register_business_request_body

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
