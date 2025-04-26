import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sepa_payment_local_instrument import SEPAPaymentLocalInstrument
from ..models.sepa_payment_sequence_type import SEPAPaymentSequenceType
from ..models.sepa_payment_type import SEPAPaymentType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SEPAPayment")


@_attrs_define
class SEPAPayment:
    amount: int
    """ Amount in cents (e.g. "150" = 1.50€) """
    debitor_iban: Union[None, str]
    """ Mandatory if type is DEBIT. If type is CREDIT, this field is overwritten with the selected bank account data
    on export. """
    debitor_name: Union[None, str]
    """ Mandatory if type is DEBIT. If type is CREDIT, this field is overwritten with the selected bank account data
    on export. """
    document_id: int
    local_instrument: SEPAPaymentLocalInstrument
    """ CORE: SEPA Core Direct Debit<br/> COR1: SEPA-Basislastschrift COR1 (deprecated use CORE instead)<br/> B2B:
    SEPA Business to Business Direct Debit """
    mandate_date_of_signature: datetime.date
    mandate_id: str
    reference: str
    sequence_type: SEPAPaymentSequenceType
    """ FRST: Erstlastschrift<br/> RCUR: Folgelastschrift<br/> OOFF: Einmallastschrift<br/> FNAL: Letztmalige
    Lastschrift """
    created_at: Union[Unset, datetime.datetime] = UNSET
    creditor_bic: Union[None, Unset, str] = UNSET
    """ If type is DEBIT, this field is overwritten with the selected bank account data on export. """
    creditor_iban: Union[None, Unset, str] = UNSET
    """ Mandatory if type is CREDIT. If type is DEBIT, this field is overwritten with the selected bank account data
    on export. """
    creditor_name: Union[None, Unset, str] = UNSET
    """ Mandatory if type is CREDIT. If type is DEBIT, this field is overwritten with the selected bank account data
    on export. """
    debitor_bic: Union[None, Unset, str] = UNSET
    """ If type is CREDIT, this field is overwritten with the selected bank account data on export. """
    debitor_address_line_1: Union[Unset, str] = UNSET
    """ Mandatory if type is DEBIT and the debitor's IBAN belongs to a country outside the EEA """
    debitor_address_line2: Union[Unset, str] = UNSET
    """ string """
    debitor_country: Union[Unset, str] = UNSET
    """ Mandatory if type is DEBIT and the debitor's IBAN belongs to a country outside the EEA """
    export_at: Union[None, Unset, datetime.datetime] = UNSET
    """ If a date is set, this record is marked as exported """
    export_error: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    remittance_information: Union[None, Unset, str] = UNSET
    requested_at: Union[Unset, datetime.date] = UNSET
    """ Booking date """
    updated_at: Union[Unset, str] = UNSET
    type_: Union[Unset, SEPAPaymentType] = SEPAPaymentType.DEBIT
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        debitor_iban: Union[None, str]
        debitor_iban = self.debitor_iban

        debitor_name: Union[None, str]
        debitor_name = self.debitor_name

        document_id = self.document_id

        local_instrument = self.local_instrument.value

        mandate_date_of_signature = self.mandate_date_of_signature.isoformat()

        mandate_id = self.mandate_id

        reference = self.reference

        sequence_type = self.sequence_type.value

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        creditor_bic: Union[None, Unset, str]
        if isinstance(self.creditor_bic, Unset):
            creditor_bic = UNSET
        else:
            creditor_bic = self.creditor_bic

        creditor_iban: Union[None, Unset, str]
        if isinstance(self.creditor_iban, Unset):
            creditor_iban = UNSET
        else:
            creditor_iban = self.creditor_iban

        creditor_name: Union[None, Unset, str]
        if isinstance(self.creditor_name, Unset):
            creditor_name = UNSET
        else:
            creditor_name = self.creditor_name

        debitor_bic: Union[None, Unset, str]
        if isinstance(self.debitor_bic, Unset):
            debitor_bic = UNSET
        else:
            debitor_bic = self.debitor_bic

        debitor_address_line_1 = self.debitor_address_line_1

        debitor_address_line2 = self.debitor_address_line2

        debitor_country = self.debitor_country

        export_at: Union[None, Unset, str]
        if isinstance(self.export_at, Unset):
            export_at = UNSET
        elif isinstance(self.export_at, datetime.datetime):
            export_at = self.export_at.isoformat()
        else:
            export_at = self.export_at

        export_error = self.export_error

        id = self.id

        remittance_information: Union[None, Unset, str]
        if isinstance(self.remittance_information, Unset):
            remittance_information = UNSET
        else:
            remittance_information = self.remittance_information

        requested_at: Union[Unset, str] = UNSET
        if not isinstance(self.requested_at, Unset):
            requested_at = self.requested_at.isoformat()

        updated_at = self.updated_at

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "amount": amount,
                "debitor_iban": debitor_iban,
                "debitor_name": debitor_name,
                "document_id": document_id,
                "local_instrument": local_instrument,
                "mandate_date_of_signature": mandate_date_of_signature,
                "mandate_id": mandate_id,
                "reference": reference,
                "sequence_type": sequence_type,
            }
        )
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if creditor_bic is not UNSET:
            field_dict["creditor_bic"] = creditor_bic
        if creditor_iban is not UNSET:
            field_dict["creditor_iban"] = creditor_iban
        if creditor_name is not UNSET:
            field_dict["creditor_name"] = creditor_name
        if debitor_bic is not UNSET:
            field_dict["debitor_bic"] = debitor_bic
        if debitor_address_line_1 is not UNSET:
            field_dict["debitor_address_line_1"] = debitor_address_line_1
        if debitor_address_line2 is not UNSET:
            field_dict["debitor_address_line2"] = debitor_address_line2
        if debitor_country is not UNSET:
            field_dict["debitor_country"] = debitor_country
        if export_at is not UNSET:
            field_dict["export_at"] = export_at
        if export_error is not UNSET:
            field_dict["export_error"] = export_error
        if id is not UNSET:
            field_dict["id"] = id
        if remittance_information is not UNSET:
            field_dict["remittance_information"] = remittance_information
        if requested_at is not UNSET:
            field_dict["requested_at"] = requested_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount")

        def _parse_debitor_iban(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        debitor_iban = _parse_debitor_iban(d.pop("debitor_iban"))

        def _parse_debitor_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        debitor_name = _parse_debitor_name(d.pop("debitor_name"))

        document_id = d.pop("document_id")

        local_instrument = SEPAPaymentLocalInstrument(d.pop("local_instrument"))

        mandate_date_of_signature = isoparse(d.pop("mandate_date_of_signature")).date()

        mandate_id = d.pop("mandate_id")

        reference = d.pop("reference")

        sequence_type = SEPAPaymentSequenceType(d.pop("sequence_type"))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_creditor_bic(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        creditor_bic = _parse_creditor_bic(d.pop("creditor_bic", UNSET))

        def _parse_creditor_iban(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        creditor_iban = _parse_creditor_iban(d.pop("creditor_iban", UNSET))

        def _parse_creditor_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        creditor_name = _parse_creditor_name(d.pop("creditor_name", UNSET))

        def _parse_debitor_bic(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        debitor_bic = _parse_debitor_bic(d.pop("debitor_bic", UNSET))

        debitor_address_line_1 = d.pop("debitor_address_line_1", UNSET)

        debitor_address_line2 = d.pop("debitor_address_line2", UNSET)

        debitor_country = d.pop("debitor_country", UNSET)

        def _parse_export_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                export_at_type_0 = isoparse(data)

                return export_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        export_at = _parse_export_at(d.pop("export_at", UNSET))

        export_error = d.pop("export_error", UNSET)

        id = d.pop("id", UNSET)

        def _parse_remittance_information(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        remittance_information = _parse_remittance_information(d.pop("remittance_information", UNSET))

        _requested_at = d.pop("requested_at", UNSET)
        requested_at: Union[Unset, datetime.date]
        if isinstance(_requested_at, Unset):
            requested_at = UNSET
        else:
            requested_at = isoparse(_requested_at).date()

        updated_at = d.pop("updated_at", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, SEPAPaymentType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = SEPAPaymentType(_type_)

        sepa_payment = cls(
            amount=amount,
            debitor_iban=debitor_iban,
            debitor_name=debitor_name,
            document_id=document_id,
            local_instrument=local_instrument,
            mandate_date_of_signature=mandate_date_of_signature,
            mandate_id=mandate_id,
            reference=reference,
            sequence_type=sequence_type,
            created_at=created_at,
            creditor_bic=creditor_bic,
            creditor_iban=creditor_iban,
            creditor_name=creditor_name,
            debitor_bic=debitor_bic,
            debitor_address_line_1=debitor_address_line_1,
            debitor_address_line2=debitor_address_line2,
            debitor_country=debitor_country,
            export_at=export_at,
            export_error=export_error,
            id=id,
            remittance_information=remittance_information,
            requested_at=requested_at,
            updated_at=updated_at,
            type_=type_,
        )

        sepa_payment.additional_properties = d
        return sepa_payment

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
