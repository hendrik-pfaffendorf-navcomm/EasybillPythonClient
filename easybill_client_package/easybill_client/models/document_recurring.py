import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.document_recurring_frequency import DocumentRecurringFrequency
from ..models.document_recurring_frequency_special import DocumentRecurringFrequencySpecial
from ..models.document_recurring_paid_date_option import DocumentRecurringPaidDateOption
from ..models.document_recurring_send_as import DocumentRecurringSendAs
from ..models.document_recurring_sepa_local_instrument import DocumentRecurringSepaLocalInstrument
from ..models.document_recurring_sepa_sequence_type import DocumentRecurringSepaSequenceType
from ..models.document_recurring_status import DocumentRecurringStatus
from ..models.document_recurring_target_type import DocumentRecurringTargetType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentRecurring")


@_attrs_define
class DocumentRecurring:
    """This object is only available in document type RECURRING."""

    next_date: datetime.date
    """ Must be in the future """
    frequency: Union[Unset, DocumentRecurringFrequency] = DocumentRecurringFrequency.MONTHLY
    frequency_special: Union[Unset, DocumentRecurringFrequencySpecial] = UNSET
    interval: Union[Unset, int] = UNSET
    end_date_or_count: Union[None, Unset, str] = UNSET
    """ Date of last exectution day or number of times to exectute """
    status: Union[Unset, DocumentRecurringStatus] = DocumentRecurringStatus.WAITING
    as_draft: Union[Unset, bool] = False
    is_notify: Union[Unset, bool] = False
    send_as: Union[Unset, DocumentRecurringSendAs] = UNSET
    is_sign: Union[Unset, bool] = False
    is_paid: Union[Unset, bool] = False
    paid_date_option: Union[Unset, DocumentRecurringPaidDateOption] = DocumentRecurringPaidDateOption.CREATED_DATE
    """ Option is used to determine what date is used for the payment if is_paid is true. "next_valid_date" selects
    the next workday in regards to the created date of the document if the date falls on a saturday or sunday. """
    is_sepa: Union[Unset, bool] = False
    sepa_local_instrument: Union[Unset, DocumentRecurringSepaLocalInstrument] = UNSET
    """ COR1 is deprecated use CORE instead. """
    sepa_sequence_type: Union[Unset, DocumentRecurringSepaSequenceType] = UNSET
    sepa_reference: Union[None, Unset, str] = UNSET
    sepa_remittance_information: Union[None, Unset, str] = UNSET
    target_type: Union[Unset, DocumentRecurringTargetType] = DocumentRecurringTargetType.INVOICE
    """ The document type that will be generated. Can not be changed on existing documents. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_date = self.next_date.isoformat()

        frequency: Union[Unset, str] = UNSET
        if not isinstance(self.frequency, Unset):
            frequency = self.frequency.value

        frequency_special: Union[Unset, str] = UNSET
        if not isinstance(self.frequency_special, Unset):
            frequency_special = self.frequency_special.value

        interval = self.interval

        end_date_or_count: Union[None, Unset, str]
        if isinstance(self.end_date_or_count, Unset):
            end_date_or_count = UNSET
        else:
            end_date_or_count = self.end_date_or_count

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        as_draft = self.as_draft

        is_notify = self.is_notify

        send_as: Union[Unset, str] = UNSET
        if not isinstance(self.send_as, Unset):
            send_as = self.send_as.value

        is_sign = self.is_sign

        is_paid = self.is_paid

        paid_date_option: Union[Unset, str] = UNSET
        if not isinstance(self.paid_date_option, Unset):
            paid_date_option = self.paid_date_option.value

        is_sepa = self.is_sepa

        sepa_local_instrument: Union[Unset, str] = UNSET
        if not isinstance(self.sepa_local_instrument, Unset):
            sepa_local_instrument = self.sepa_local_instrument.value

        sepa_sequence_type: Union[Unset, str] = UNSET
        if not isinstance(self.sepa_sequence_type, Unset):
            sepa_sequence_type = self.sepa_sequence_type.value

        sepa_reference: Union[None, Unset, str]
        if isinstance(self.sepa_reference, Unset):
            sepa_reference = UNSET
        else:
            sepa_reference = self.sepa_reference

        sepa_remittance_information: Union[None, Unset, str]
        if isinstance(self.sepa_remittance_information, Unset):
            sepa_remittance_information = UNSET
        else:
            sepa_remittance_information = self.sepa_remittance_information

        target_type: Union[Unset, str] = UNSET
        if not isinstance(self.target_type, Unset):
            target_type = self.target_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "next_date": next_date,
            }
        )
        if frequency is not UNSET:
            field_dict["frequency"] = frequency
        if frequency_special is not UNSET:
            field_dict["frequency_special"] = frequency_special
        if interval is not UNSET:
            field_dict["interval"] = interval
        if end_date_or_count is not UNSET:
            field_dict["end_date_or_count"] = end_date_or_count
        if status is not UNSET:
            field_dict["status"] = status
        if as_draft is not UNSET:
            field_dict["as_draft"] = as_draft
        if is_notify is not UNSET:
            field_dict["is_notify"] = is_notify
        if send_as is not UNSET:
            field_dict["send_as"] = send_as
        if is_sign is not UNSET:
            field_dict["is_sign"] = is_sign
        if is_paid is not UNSET:
            field_dict["is_paid"] = is_paid
        if paid_date_option is not UNSET:
            field_dict["paid_date_option"] = paid_date_option
        if is_sepa is not UNSET:
            field_dict["is_sepa"] = is_sepa
        if sepa_local_instrument is not UNSET:
            field_dict["sepa_local_instrument"] = sepa_local_instrument
        if sepa_sequence_type is not UNSET:
            field_dict["sepa_sequence_type"] = sepa_sequence_type
        if sepa_reference is not UNSET:
            field_dict["sepa_reference"] = sepa_reference
        if sepa_remittance_information is not UNSET:
            field_dict["sepa_remittance_information"] = sepa_remittance_information
        if target_type is not UNSET:
            field_dict["target_type"] = target_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        next_date = isoparse(d.pop("next_date")).date()

        _frequency = d.pop("frequency", UNSET)
        frequency: Union[Unset, DocumentRecurringFrequency]
        if isinstance(_frequency, Unset):
            frequency = UNSET
        else:
            frequency = DocumentRecurringFrequency(_frequency)

        _frequency_special = d.pop("frequency_special", UNSET)
        frequency_special: Union[Unset, DocumentRecurringFrequencySpecial]
        if isinstance(_frequency_special, Unset):
            frequency_special = UNSET
        else:
            frequency_special = DocumentRecurringFrequencySpecial(_frequency_special)

        interval = d.pop("interval", UNSET)

        def _parse_end_date_or_count(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        end_date_or_count = _parse_end_date_or_count(d.pop("end_date_or_count", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, DocumentRecurringStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DocumentRecurringStatus(_status)

        as_draft = d.pop("as_draft", UNSET)

        is_notify = d.pop("is_notify", UNSET)

        _send_as = d.pop("send_as", UNSET)
        send_as: Union[Unset, DocumentRecurringSendAs]
        if isinstance(_send_as, Unset):
            send_as = UNSET
        else:
            send_as = DocumentRecurringSendAs(_send_as)

        is_sign = d.pop("is_sign", UNSET)

        is_paid = d.pop("is_paid", UNSET)

        _paid_date_option = d.pop("paid_date_option", UNSET)
        paid_date_option: Union[Unset, DocumentRecurringPaidDateOption]
        if isinstance(_paid_date_option, Unset):
            paid_date_option = UNSET
        else:
            paid_date_option = DocumentRecurringPaidDateOption(_paid_date_option)

        is_sepa = d.pop("is_sepa", UNSET)

        _sepa_local_instrument = d.pop("sepa_local_instrument", UNSET)
        sepa_local_instrument: Union[Unset, DocumentRecurringSepaLocalInstrument]
        if isinstance(_sepa_local_instrument, Unset):
            sepa_local_instrument = UNSET
        else:
            sepa_local_instrument = DocumentRecurringSepaLocalInstrument(_sepa_local_instrument)

        _sepa_sequence_type = d.pop("sepa_sequence_type", UNSET)
        sepa_sequence_type: Union[Unset, DocumentRecurringSepaSequenceType]
        if isinstance(_sepa_sequence_type, Unset):
            sepa_sequence_type = UNSET
        else:
            sepa_sequence_type = DocumentRecurringSepaSequenceType(_sepa_sequence_type)

        def _parse_sepa_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_reference = _parse_sepa_reference(d.pop("sepa_reference", UNSET))

        def _parse_sepa_remittance_information(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_remittance_information = _parse_sepa_remittance_information(d.pop("sepa_remittance_information", UNSET))

        _target_type = d.pop("target_type", UNSET)
        target_type: Union[Unset, DocumentRecurringTargetType]
        if isinstance(_target_type, Unset):
            target_type = UNSET
        else:
            target_type = DocumentRecurringTargetType(_target_type)

        document_recurring = cls(
            next_date=next_date,
            frequency=frequency,
            frequency_special=frequency_special,
            interval=interval,
            end_date_or_count=end_date_or_count,
            status=status,
            as_draft=as_draft,
            is_notify=is_notify,
            send_as=send_as,
            is_sign=is_sign,
            is_paid=is_paid,
            paid_date_option=paid_date_option,
            is_sepa=is_sepa,
            sepa_local_instrument=sepa_local_instrument,
            sepa_sequence_type=sepa_sequence_type,
            sepa_reference=sepa_reference,
            sepa_remittance_information=sepa_remittance_information,
            target_type=target_type,
        )

        document_recurring.additional_properties = d
        return document_recurring

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
