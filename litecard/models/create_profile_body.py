from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateProfileBody")


@_attrs_define
class CreateProfileBody:
    """
    Attributes:
        business_name (Union[Unset, str]): Business name Example: Cryo gym.
        sub_business_name (Union[Unset, str]): Name to show on sub business selection Example: Cryo gym - Sub 1.
        email (Union[Unset, str]): Business email Example: Ankus Fang.
        post_code (Union[Unset, str]): Business postcode Example: CryoGym.
        state (Union[Unset, str]): Business state Example: AHVW1qv4I_Teqdu4VjwMA.
        logo_image (Union[None, Unset, str]): Business logo image file Example: CryoGym.
        template_count (Union[Unset, float]): Current total number of templates a user has. Example: 3.
        template_limit (Union[Unset, float]): Maximum amount of templates this user can have. A templateLimit of -1
            means the user can have unlimited templates. Example: 12.
        created_at (Union[Unset, str]): Date when pass was first created, in ISO-8601 format Example:
            2021-08-11T03:15:56.860Z.
        updated_at (Union[Unset, str]): Date when pass was last updated, in ISO-8601 format Example:
            2021-08-1T03:15:56.860Z.
        is_master_business (Union[Unset, bool]): Is the account a master account Example: True.
        master_business_id (Union[Unset, str]): Master business id Example: master-business-id.
    """

    business_name: Union[Unset, str] = UNSET
    sub_business_name: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    post_code: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    logo_image: Union[None, Unset, str] = UNSET
    template_count: Union[Unset, float] = UNSET
    template_limit: Union[Unset, float] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    is_master_business: Union[Unset, bool] = UNSET
    master_business_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        business_name = self.business_name

        sub_business_name = self.sub_business_name

        email = self.email

        post_code = self.post_code

        state = self.state

        logo_image: Union[None, Unset, str]
        if isinstance(self.logo_image, Unset):
            logo_image = UNSET
        else:
            logo_image = self.logo_image

        template_count = self.template_count

        template_limit = self.template_limit

        created_at = self.created_at

        updated_at = self.updated_at

        is_master_business = self.is_master_business

        master_business_id = self.master_business_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if business_name is not UNSET:
            field_dict["businessName"] = business_name
        if sub_business_name is not UNSET:
            field_dict["subBusinessName"] = sub_business_name
        if email is not UNSET:
            field_dict["email"] = email
        if post_code is not UNSET:
            field_dict["postCode"] = post_code
        if state is not UNSET:
            field_dict["state"] = state
        if logo_image is not UNSET:
            field_dict["logoImage"] = logo_image
        if template_count is not UNSET:
            field_dict["templateCount"] = template_count
        if template_limit is not UNSET:
            field_dict["templateLimit"] = template_limit
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if is_master_business is not UNSET:
            field_dict["isMasterBusiness"] = is_master_business
        if master_business_id is not UNSET:
            field_dict["masterBusinessId"] = master_business_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        business_name = d.pop("businessName", UNSET)

        sub_business_name = d.pop("subBusinessName", UNSET)

        email = d.pop("email", UNSET)

        post_code = d.pop("postCode", UNSET)

        state = d.pop("state", UNSET)

        def _parse_logo_image(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        logo_image = _parse_logo_image(d.pop("logoImage", UNSET))

        template_count = d.pop("templateCount", UNSET)

        template_limit = d.pop("templateLimit", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        is_master_business = d.pop("isMasterBusiness", UNSET)

        master_business_id = d.pop("masterBusinessId", UNSET)

        create_profile_body = cls(
            business_name=business_name,
            sub_business_name=sub_business_name,
            email=email,
            post_code=post_code,
            state=state,
            logo_image=logo_image,
            template_count=template_count,
            template_limit=template_limit,
            created_at=created_at,
            updated_at=updated_at,
            is_master_business=is_master_business,
            master_business_id=master_business_id,
        )

        create_profile_body.additional_properties = d
        return create_profile_body

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
