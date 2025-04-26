import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.post_box_document_file_type import PostBoxDocumentFileType
from ..models.post_box_post_send_type import PostBoxPostSendType
from ..models.post_box_status import PostBoxStatus
from ..models.post_box_type import PostBoxType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostBox")


@_attrs_define
class PostBox:
    id: Union[Unset, int] = UNSET
    document_id: Union[Unset, int] = UNSET
    to: Union[Unset, str] = UNSET
    cc: Union[Unset, str] = UNSET
    from_: Union[Unset, str] = UNSET
    subject: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.date] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    processed_at: Union[Unset, datetime.datetime] = UNSET
    send_by_self: Union[Unset, bool] = UNSET
    send_with_attachment: Union[Unset, bool] = UNSET
    type_: Union[Unset, PostBoxType] = UNSET
    status: Union[Unset, PostBoxStatus] = UNSET
    status_msg: Union[Unset, str] = UNSET
    login_id: Union[Unset, int] = UNSET
    document_file_type: Union[Unset, PostBoxDocumentFileType] = UNSET
    post_send_type: Union[Unset, PostBoxPostSendType] = UNSET
    """ This value indicates what method is used when the document is send via mail.
    The different types are offered by the german post as additional services.
    The registered mail options will include a tracking number which will be
    added to the postbox when known.

    If the value is omitted or empty when a postbox is created with the type "POST"
    post_send_type_standard will be used.

    For postbox with a different type than "POST" this field will hold a empty string.
     """
    tracking_identifier: Union[Unset, str] = UNSET
    """ If the document is send with one of the registered send types stated for post_send_type, a tracking
    identifier
    will be added to the postbox at a later point when the tracking identifier is provided
    by our service partner.
     """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        document_id = self.document_id

        to = self.to

        cc = self.cc

        from_ = self.from_

        subject = self.subject

        message = self.message

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        processed_at: Union[Unset, str] = UNSET
        if not isinstance(self.processed_at, Unset):
            processed_at = self.processed_at.isoformat()

        send_by_self = self.send_by_self

        send_with_attachment = self.send_with_attachment

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        status_msg = self.status_msg

        login_id = self.login_id

        document_file_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_file_type, Unset):
            document_file_type = self.document_file_type.value

        post_send_type: Union[Unset, str] = UNSET
        if not isinstance(self.post_send_type, Unset):
            post_send_type = self.post_send_type.value

        tracking_identifier = self.tracking_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
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
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if processed_at is not UNSET:
            field_dict["processed_at"] = processed_at
        if send_by_self is not UNSET:
            field_dict["send_by_self"] = send_by_self
        if send_with_attachment is not UNSET:
            field_dict["send_with_attachment"] = send_with_attachment
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if status_msg is not UNSET:
            field_dict["status_msg"] = status_msg
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if document_file_type is not UNSET:
            field_dict["document_file_type"] = document_file_type
        if post_send_type is not UNSET:
            field_dict["post_send_type"] = post_send_type
        if tracking_identifier is not UNSET:
            field_dict["tracking_identifier"] = tracking_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        document_id = d.pop("document_id", UNSET)

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

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        _processed_at = d.pop("processed_at", UNSET)
        processed_at: Union[Unset, datetime.datetime]
        if isinstance(_processed_at, Unset):
            processed_at = UNSET
        else:
            processed_at = isoparse(_processed_at)

        send_by_self = d.pop("send_by_self", UNSET)

        send_with_attachment = d.pop("send_with_attachment", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PostBoxType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PostBoxType(_type_)

        _status = d.pop("status", UNSET)
        status: Union[Unset, PostBoxStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = PostBoxStatus(_status)

        status_msg = d.pop("status_msg", UNSET)

        login_id = d.pop("login_id", UNSET)

        _document_file_type = d.pop("document_file_type", UNSET)
        document_file_type: Union[Unset, PostBoxDocumentFileType]
        if isinstance(_document_file_type, Unset):
            document_file_type = UNSET
        else:
            document_file_type = PostBoxDocumentFileType(_document_file_type)

        _post_send_type = d.pop("post_send_type", UNSET)
        post_send_type: Union[Unset, PostBoxPostSendType]
        if isinstance(_post_send_type, Unset):
            post_send_type = UNSET
        else:
            post_send_type = PostBoxPostSendType(_post_send_type)

        tracking_identifier = d.pop("tracking_identifier", UNSET)

        post_box = cls(
            id=id,
            document_id=document_id,
            to=to,
            cc=cc,
            from_=from_,
            subject=subject,
            message=message,
            date=date,
            created_at=created_at,
            processed_at=processed_at,
            send_by_self=send_by_self,
            send_with_attachment=send_with_attachment,
            type_=type_,
            status=status,
            status_msg=status_msg,
            login_id=login_id,
            document_file_type=document_file_type,
            post_send_type=post_send_type,
            tracking_identifier=tracking_identifier,
        )

        post_box.additional_properties = d
        return post_box

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
