from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Contact")


@_attrs_define
class Contact:
    city: str
    street: str
    state: Union[Unset, str] = UNSET
    company_name: Union[None, Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    """ Two-letter country code """
    department: Union[None, Unset, str] = UNSET
    emails: Union[Unset, list[str]] = UNSET
    fax: Union[None, Unset, str] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    last_name: Union[None, Unset, str] = UNSET
    login_id: Union[Unset, int] = UNSET
    mobile: Union[None, Unset, str] = UNSET
    note: Union[None, Unset, str] = UNSET
    personal: Union[Unset, bool] = False
    phone_1: Union[None, Unset, str] = UNSET
    phone_2: Union[None, Unset, str] = UNSET
    salutation: Union[Unset, int] = UNSET
    """ 0: empty<br/> 1: Herrn<br/> 2: Frau<br/> 3: Firma<br/> 4: Herrn und Frau<br/> 5: Eheleute<br/> 6: Familie
    """
    suffix_1: Union[None, Unset, str] = UNSET
    suffix_2: Union[None, Unset, str] = UNSET
    title: Union[None, Unset, str] = UNSET
    zip_code: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        city = self.city

        street = self.street

        state = self.state

        company_name: Union[None, Unset, str]
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        country = self.country

        department: Union[None, Unset, str]
        if isinstance(self.department, Unset):
            department = UNSET
        else:
            department = self.department

        emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        fax: Union[None, Unset, str]
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        id = self.id

        last_name: Union[None, Unset, str]
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        login_id = self.login_id

        mobile: Union[None, Unset, str]
        if isinstance(self.mobile, Unset):
            mobile = UNSET
        else:
            mobile = self.mobile

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        personal = self.personal

        phone_1: Union[None, Unset, str]
        if isinstance(self.phone_1, Unset):
            phone_1 = UNSET
        else:
            phone_1 = self.phone_1

        phone_2: Union[None, Unset, str]
        if isinstance(self.phone_2, Unset):
            phone_2 = UNSET
        else:
            phone_2 = self.phone_2

        salutation = self.salutation

        suffix_1: Union[None, Unset, str]
        if isinstance(self.suffix_1, Unset):
            suffix_1 = UNSET
        else:
            suffix_1 = self.suffix_1

        suffix_2: Union[None, Unset, str]
        if isinstance(self.suffix_2, Unset):
            suffix_2 = UNSET
        else:
            suffix_2 = self.suffix_2

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        zip_code: Union[None, Unset, str]
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "city": city,
                "street": street,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if country is not UNSET:
            field_dict["country"] = country
        if department is not UNSET:
            field_dict["department"] = department
        if emails is not UNSET:
            field_dict["emails"] = emails
        if fax is not UNSET:
            field_dict["fax"] = fax
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if note is not UNSET:
            field_dict["note"] = note
        if personal is not UNSET:
            field_dict["personal"] = personal
        if phone_1 is not UNSET:
            field_dict["phone_1"] = phone_1
        if phone_2 is not UNSET:
            field_dict["phone_2"] = phone_2
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if suffix_1 is not UNSET:
            field_dict["suffix_1"] = suffix_1
        if suffix_2 is not UNSET:
            field_dict["suffix_2"] = suffix_2
        if title is not UNSET:
            field_dict["title"] = title
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        city = d.pop("city")

        street = d.pop("street")

        state = d.pop("state", UNSET)

        def _parse_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        country = d.pop("country", UNSET)

        def _parse_department(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        department = _parse_department(d.pop("department", UNSET))

        emails = cast(list[str], d.pop("emails", UNSET))

        def _parse_fax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

        id = d.pop("id", UNSET)

        def _parse_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))

        login_id = d.pop("login_id", UNSET)

        def _parse_mobile(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mobile = _parse_mobile(d.pop("mobile", UNSET))

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        personal = d.pop("personal", UNSET)

        def _parse_phone_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_1 = _parse_phone_1(d.pop("phone_1", UNSET))

        def _parse_phone_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_2 = _parse_phone_2(d.pop("phone_2", UNSET))

        salutation = d.pop("salutation", UNSET)

        def _parse_suffix_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suffix_1 = _parse_suffix_1(d.pop("suffix_1", UNSET))

        def _parse_suffix_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suffix_2 = _parse_suffix_2(d.pop("suffix_2", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        def _parse_zip_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zip_code = _parse_zip_code(d.pop("zip_code", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        contact = cls(
            city=city,
            street=street,
            state=state,
            company_name=company_name,
            country=country,
            department=department,
            emails=emails,
            fax=fax,
            first_name=first_name,
            id=id,
            last_name=last_name,
            login_id=login_id,
            mobile=mobile,
            note=note,
            personal=personal,
            phone_1=phone_1,
            phone_2=phone_2,
            salutation=salutation,
            suffix_1=suffix_1,
            suffix_2=suffix_2,
            title=title,
            zip_code=zip_code,
            created_at=created_at,
            updated_at=updated_at,
        )

        contact.additional_properties = d
        return contact

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
