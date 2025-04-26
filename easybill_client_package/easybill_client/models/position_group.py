from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionGroup")


@_attrs_define
class PositionGroup:
    name: str
    number: str
    description: Union[None, Unset, str] = UNSET
    login_id: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        number = self.number

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        login_id = self.login_id

        display_name = self.display_name

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "number": number,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        number = d.pop("number")

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        login_id = d.pop("login_id", UNSET)

        display_name = d.pop("display_name", UNSET)

        id = d.pop("id", UNSET)

        position_group = cls(
            name=name,
            number=number,
            description=description,
            login_id=login_id,
            display_name=display_name,
            id=id,
        )

        position_group.additional_properties = d
        return position_group

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
