from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TextTemplate")


@_attrs_define
class TextTemplate:
    text: str
    title: str
    can_modify: Union[Unset, bool] = UNSET
    """ Deprecated, field is always true. """
    id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text = self.text

        title = self.title

        can_modify = self.can_modify

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
                "title": title,
            }
        )
        if can_modify is not UNSET:
            field_dict["can_modify"] = can_modify
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        title = d.pop("title")

        can_modify = d.pop("can_modify", UNSET)

        id = d.pop("id", UNSET)

        text_template = cls(
            text=text,
            title=title,
            can_modify=can_modify,
            id=id,
        )

        text_template.additional_properties = d
        return text_template

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
