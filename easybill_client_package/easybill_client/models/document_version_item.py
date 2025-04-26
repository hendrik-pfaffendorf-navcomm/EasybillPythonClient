from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_version_item_document_version_item_type import DocumentVersionItemDocumentVersionItemType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentVersionItem")


@_attrs_define
class DocumentVersionItem:
    document_version_item_type: Union[Unset, DocumentVersionItemDocumentVersionItemType] = UNSET
    id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        document_version_item_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_version_item_type, Unset):
            document_version_item_type = self.document_version_item_type.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if document_version_item_type is not UNSET:
            field_dict["document_version_item_type"] = document_version_item_type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _document_version_item_type = d.pop("document_version_item_type", UNSET)
        document_version_item_type: Union[Unset, DocumentVersionItemDocumentVersionItemType]
        if isinstance(_document_version_item_type, Unset):
            document_version_item_type = UNSET
        else:
            document_version_item_type = DocumentVersionItemDocumentVersionItemType(_document_version_item_type)

        id = d.pop("id", UNSET)

        document_version_item = cls(
            document_version_item_type=document_version_item_type,
            id=id,
        )

        document_version_item.additional_properties = d
        return document_version_item

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
