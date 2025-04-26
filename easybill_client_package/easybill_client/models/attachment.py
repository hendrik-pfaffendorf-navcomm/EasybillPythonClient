import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="Attachment")


@_attrs_define
class Attachment:
    """If customer_id, project_id and document_id are null, the attachment has a global context and is accessible from the
    web ui. Keep in mind only to provide one of the four context. You can't attach a file to several context in one
    request. A error is thrown if you provide two or more context (i. E. sending customer_id, document_id and project_id
    in combination).

    """

    created_at: Union[Unset, datetime.date] = UNSET
    customer_id: Union[None, Unset, int] = UNSET
    document_id: Union[None, Unset, int] = UNSET
    file_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    project_id: Union[None, Unset, int] = UNSET
    size: Union[Unset, int] = UNSET
    """ In byte """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        customer_id: Union[None, Unset, int]
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        document_id: Union[None, Unset, int]
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        file_name = self.file_name

        id = self.id

        project_id: Union[None, Unset, int]
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if file_name is not UNSET:
            field_dict["file_name"] = file_name
        if id is not UNSET:
            field_dict["id"] = id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.date]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at).date()

        def _parse_customer_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        def _parse_document_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        file_name = d.pop("file_name", UNSET)

        id = d.pop("id", UNSET)

        def _parse_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        size = d.pop("size", UNSET)

        attachment = cls(
            created_at=created_at,
            customer_id=customer_id,
            document_id=document_id,
            file_name=file_name,
            id=id,
            project_id=project_id,
            size=size,
        )

        attachment.additional_properties = d
        return attachment

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
