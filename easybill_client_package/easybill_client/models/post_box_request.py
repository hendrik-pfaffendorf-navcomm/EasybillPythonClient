import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_box_request_document_file_type import PostBoxRequestDocumentFileType
from ..models.post_box_request_post_send_type import PostBoxRequestPostSendType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostBoxRequest")


@_attrs_define
class PostBoxRequest:
    to: Union[Unset, str] = UNSET
    cc: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    send_by_self: Union[Unset, bool] = UNSET
    send_with_attachment: Union[Unset, bool] = True
    document_file_type: Union[Unset, PostBoxRequestDocumentFileType] = UNSET
    """ When set to null, the setting on the customer is used """
    post_send_type: Union[Unset, PostBoxRequestPostSendType] = UNSET
    """ This value indicates what method is used when the document is send via mail.
    The different types are offered by the german post as additional services.
    The registered mail options will include a tracking number which will be
    added to the postbox when known.

    If the value is omitted or empty when a postbox is created with the type "POST"
    post_send_type_standard will be used.

    For postbox with a different type than "POST" this field will hold a empty string.
     """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        to = self.to

        cc = self.cc

        from_ = self.from_

        subject = self.subject

        message = self.message

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        send_by_self = self.send_by_self

        send_with_attachment = self.send_with_attachment

        document_file_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_file_type, Unset):
            document_file_type = self.document_file_type.value

        post_send_type: Union[Unset, str] = UNSET
        if not isinstance(self.post_send_type, Unset):
            post_send_type = self.post_send_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if to is not UNSET:
            field_dict["to"] = to
        if cc is not UNSET:
            field_dict["cc"] = cc
        if from_ is not UNSET:
            field_dict["from"] = from_
        if subject is not UNSET:
            field_dict["subject"] = subject
        if message is not UNSET:
            field_dict["message"] = message
        if date is not UNSET:
            field_dict["date"] = date
        if send_by_self is not UNSET:
            field_dict["send_by_self"] = send_by_self
        if send_with_attachment is not UNSET:
            field_dict["send_with_attachment"] = send_with_attachment
        if document_file_type is not UNSET:
            field_dict["document_file_type"] = document_file_type
        if post_send_type is not UNSET:
            field_dict["post_send_type"] = post_send_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        to = d.pop("to", UNSET)

        cc = d.pop("cc", UNSET)

        from_ = d.pop("from", UNSET)

        subject = d.pop("subject", UNSET)

        message = d.pop("message", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.date]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date).date()

        send_by_self = d.pop("send_by_self", UNSET)

        send_with_attachment = d.pop("send_with_attachment", UNSET)

        _document_file_type = d.pop("document_file_type", UNSET)
        document_file_type: Union[Unset, PostBoxRequestDocumentFileType]
        if isinstance(_document_file_type, Unset):
            document_file_type = UNSET
        else:
            document_file_type = PostBoxRequestDocumentFileType(_document_file_type)

        _post_send_type = d.pop("post_send_type", UNSET)
        post_send_type: Union[Unset, PostBoxRequestPostSendType]
        if isinstance(_post_send_type, Unset):
            post_send_type = UNSET
        else:
            post_send_type = PostBoxRequestPostSendType(_post_send_type)

        post_box_request = cls(
            to=to,
            cc=cc,
            from_=from_,
            subject=subject,
            message=message,
            date=date,
            send_by_self=send_by_self,
            send_with_attachment=send_with_attachment,
            document_file_type=document_file_type,
            post_send_type=post_send_type,
        )

        post_box_request.additional_properties = d
        return post_box_request

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
