from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login import Login


T = TypeVar("T", bound="Logins")


@_attrs_define
class Logins:
    page: int
    """ The current page """
    pages: int
    """ Max possible pages """
    limit: int
    """ Items limitation. Max 1000 """
    total: int
    """ Total Items """
    items: Union[Unset, list["Login"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page = self.page

        pages = self.pages

        limit = self.limit

        total = self.total

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "page": page,
                "pages": pages,
                "limit": limit,
                "total": total,
            }
        )
        if items is not UNSET:
            field_dict["items"] = items

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login import Login

        d = dict(src_dict)
        page = d.pop("page")

        pages = d.pop("pages")

        limit = d.pop("limit")

        total = d.pop("total")

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = Login.from_dict(items_item_data)

            items.append(items_item)

        logins = cls(
            page=page,
            pages=pages,
            limit=limit,
            total=total,
            items=items,
        )

        logins.additional_properties = d
        return logins

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
