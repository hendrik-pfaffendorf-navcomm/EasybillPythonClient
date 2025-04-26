from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Stock")


@_attrs_define
class Stock:
    stock_count: int
    position_id: int
    id: Union[Unset, int] = UNSET
    note: Union[Unset, str] = UNSET
    document_id: Union[None, Unset, int] = UNSET
    document_position_id: Union[None, Unset, int] = UNSET
    stored_at: Union[None, Unset, str] = UNSET
    created_at: Union[Unset, str] = UNSET
    updated_at: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stock_count = self.stock_count

        position_id = self.position_id

        id = self.id

        note = self.note

        document_id: Union[None, Unset, int]
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        document_position_id: Union[None, Unset, int]
        if isinstance(self.document_position_id, Unset):
            document_position_id = UNSET
        else:
            document_position_id = self.document_position_id

        stored_at: Union[None, Unset, str]
        if isinstance(self.stored_at, Unset):
            stored_at = UNSET
        else:
            stored_at = self.stored_at

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "stock_count": stock_count,
                "position_id": position_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if document_position_id is not UNSET:
            field_dict["document_position_id"] = document_position_id
        if stored_at is not UNSET:
            field_dict["stored_at"] = stored_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        stock_count = d.pop("stock_count")

        position_id = d.pop("position_id")

        id = d.pop("id", UNSET)

        note = d.pop("note", UNSET)

        def _parse_document_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        def _parse_document_position_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        document_position_id = _parse_document_position_id(d.pop("document_position_id", UNSET))

        def _parse_stored_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        stored_at = _parse_stored_at(d.pop("stored_at", UNSET))

        created_at = d.pop("created_at", UNSET)

        updated_at = d.pop("updated_at", UNSET)

        stock = cls(
            stock_count=stock_count,
            position_id=position_id,
            id=id,
            note=note,
            document_id=document_id,
            document_position_id=document_position_id,
            stored_at=stored_at,
            created_at=created_at,
            updated_at=updated_at,
        )

        stock.additional_properties = d
        return stock

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
