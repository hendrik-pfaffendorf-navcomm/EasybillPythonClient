from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentAddress")


@_attrs_define
class DocumentAddress:
    """This information comes from the customer which can be set with customer_id."""

    salutation: Union[Unset, int] = UNSET
    """ 0: empty<br/> 1: Herrn<br/> 2: Frau<br/> 3: Firma<br/> 4: Herrn und Frau<br/> 5: Eheleute<br/> 6: Familie
    """
    personal: Union[Unset, bool] = UNSET
    title: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    suffix_1: Union[Unset, str] = UNSET
    suffix_2: Union[Unset, str] = UNSET
    company_name: Union[Unset, str] = UNSET
    street: Union[Unset, str] = UNSET
    zip_code: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        salutation = self.salutation

        personal = self.personal

        title = self.title

        first_name = self.first_name

        last_name = self.last_name

        suffix_1 = self.suffix_1

        suffix_2 = self.suffix_2

        company_name = self.company_name

        street = self.street

        zip_code = self.zip_code

        city = self.city

        state = self.state

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if personal is not UNSET:
            field_dict["personal"] = personal
        if title is not UNSET:
            field_dict["title"] = title
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if suffix_1 is not UNSET:
            field_dict["suffix_1"] = suffix_1
        if suffix_2 is not UNSET:
            field_dict["suffix_2"] = suffix_2
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if street is not UNSET:
            field_dict["street"] = street
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        salutation = d.pop("salutation", UNSET)

        personal = d.pop("personal", UNSET)

        title = d.pop("title", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        suffix_1 = d.pop("suffix_1", UNSET)

        suffix_2 = d.pop("suffix_2", UNSET)

        company_name = d.pop("company_name", UNSET)

        street = d.pop("street", UNSET)

        zip_code = d.pop("zip_code", UNSET)

        city = d.pop("city", UNSET)

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        document_address = cls(
            salutation=salutation,
            personal=personal,
            title=title,
            first_name=first_name,
            last_name=last_name,
            suffix_1=suffix_1,
            suffix_2=suffix_2,
            company_name=company_name,
            street=street,
            zip_code=zip_code,
            city=city,
            state=state,
            country=country,
        )

        document_address.additional_properties = d
        return document_address

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
