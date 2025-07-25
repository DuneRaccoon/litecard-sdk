from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.list_certificates_response_v1 import ListCertificatesResponseV1


T = TypeVar("T", bound="GetCertificatesV1Response200")


@_attrs_define
class GetCertificatesV1Response200:
    """
    Attributes:
        certificates (Union[Unset, list['ListCertificatesResponseV1']]): Certificate metadata
        next_ (Union[Unset, str]): Key to continue pagination
    """

    certificates: Union[Unset, list["ListCertificatesResponseV1"]] = UNSET
    next_: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        certificates: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.certificates, Unset):
            certificates = []
            for certificates_item_data in self.certificates:
                certificates_item = certificates_item_data.to_dict()
                certificates.append(certificates_item)

        next_ = self.next_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if certificates is not UNSET:
            field_dict["certificates"] = certificates
        if next_ is not UNSET:
            field_dict["next"] = next_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.list_certificates_response_v1 import ListCertificatesResponseV1

        d = dict(src_dict)
        certificates = []
        _certificates = d.pop("certificates", UNSET)
        for certificates_item_data in _certificates or []:
            certificates_item = ListCertificatesResponseV1.from_dict(certificates_item_data)

            certificates.append(certificates_item)

        next_ = d.pop("next", UNSET)

        get_certificates_v1_response_200 = cls(
            certificates=certificates,
            next_=next_,
        )

        get_certificates_v1_response_200.additional_properties = d
        return get_certificates_v1_response_200

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
