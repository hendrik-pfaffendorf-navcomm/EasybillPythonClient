import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentPayment")


@_attrs_define
class DocumentPayment:
    """
    Example:
        {'id': 1, 'document_id': 1, 'login_id': 1, 'amount': 1000, 'payment_at': datetime.datetime(2007, 9, 17, 0, 0,
            tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'type': 'VISA', 'provider': 'Stripe', 'reference':
            '111111-VISA-222222-6666'}

    """

    amount: int
    document_id: int
    id: Union[Unset, int] = UNSET
    is_overdue_fee: Union[Unset, bool] = UNSET
    login_id: Union[Unset, int] = UNSET
    notice: Union[Unset, str] = ""
    payment_at: Union[Unset, datetime.date] = UNSET
    type_: Union[Unset, str] = ""
    provider: Union[Unset, str] = ""
    reference: Union[Unset, str] = ""
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        document_id = self.document_id

        id = self.id

        is_overdue_fee = self.is_overdue_fee

        login_id = self.login_id

        notice = self.notice

        payment_at: Union[Unset, str] = UNSET
        if not isinstance(self.payment_at, Unset):
            payment_at = self.payment_at.isoformat()

        type_ = self.type_

        provider = self.provider

        reference = self.reference

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "document_id": document_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_overdue_fee is not UNSET:
            field_dict["is_overdue_fee"] = is_overdue_fee
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if notice is not UNSET:
            field_dict["notice"] = notice
        if payment_at is not UNSET:
            field_dict["payment_at"] = payment_at
        if type_ is not UNSET:
            field_dict["type"] = type_
        if provider is not UNSET:
            field_dict["provider"] = provider
        if reference is not UNSET:
            field_dict["reference"] = reference

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        document_id = d.pop("document_id")

        id = d.pop("id", UNSET)

        is_overdue_fee = d.pop("is_overdue_fee", UNSET)

        login_id = d.pop("login_id", UNSET)

        notice = d.pop("notice", UNSET)

        _payment_at = d.pop("payment_at", UNSET)
        payment_at: Union[Unset, datetime.date]
        if isinstance(_payment_at, Unset):
            payment_at = UNSET
        else:
            payment_at = isoparse(_payment_at).date()

        type_ = d.pop("type", UNSET)

        provider = d.pop("provider", UNSET)

        reference = d.pop("reference", UNSET)

        document_payment = cls(
            amount=amount,
            document_id=document_id,
            id=id,
            is_overdue_fee=is_overdue_fee,
            login_id=login_id,
            notice=notice,
            payment_at=payment_at,
            type_=type_,
            provider=provider,
            reference=reference,
        )

        document_payment.additional_properties = d
        return document_payment

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
