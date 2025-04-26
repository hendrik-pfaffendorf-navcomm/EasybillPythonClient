import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.document_anonymize_status import DocumentAnonymizeStatus
from ..models.document_discount_type import DocumentDiscountType
from ..models.document_status import DocumentStatus
from ..models.document_type import DocumentType
from ..models.document_vat_option import DocumentVatOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.customer import Customer
    from ..models.document_address import DocumentAddress
    from ..models.document_position import DocumentPosition
    from ..models.document_recurring import DocumentRecurring
    from ..models.file_format_config import FileFormatConfig
    from ..models.service_date import ServiceDate


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    address: Union[Unset, "DocumentAddress"] = UNSET
    """ This information comes from the customer which can be set with customer_id. """
    attachment_ids: Union[Unset, list[int]] = UNSET
    label_address: Union[Unset, "DocumentAddress"] = UNSET
    """ This information comes from the customer which can be set with customer_id. """
    amount: Union[Unset, int] = UNSET
    """ Amount in cents  (e.g. "150" = 1.50€) """
    amount_net: Union[Unset, int] = UNSET
    """ Amount in cents  (e.g. "150" = 1.50€) """
    anonymize_due_date: Union[None, Unset, datetime.date] = UNSET
    """ A date which signals when to anonymize the document. Must be in the future. Turns into a read only field if
    the document is anonymized """
    anonymize_status: Union[Unset, DocumentAnonymizeStatus] = DocumentAnonymizeStatus.NOT_ANONYMIZED
    """ This field signals if the document was anonymized """
    anonymized_at: Union[None, Unset, str] = UNSET
    bank_debit_form: Union[None, Unset, str] = UNSET
    billing_country: Union[Unset, str] = UNSET
    calc_vat_from: Union[Unset, int] = UNSET
    """ 0 === Net, 1 === Gross. """
    cancel_id: Union[Unset, int] = UNSET
    """ ID from the cancel document. Only for document type INVOICE. """
    cash_allowance: Union[None, Unset, float] = UNSET
    cash_allowance_days: Union[None, Unset, int] = UNSET
    cash_allowance_text: Union[None, Unset, str] = UNSET
    contact_id: Union[None, Unset, int] = UNSET
    contact_label: Union[Unset, str] = ""
    contact_text: Union[Unset, str] = ""
    created_at: Union[Unset, datetime.datetime] = UNSET
    currency: Union[Unset, str] = "EUR"
    customer_id: Union[None, Unset, int] = UNSET
    customer_snapshot: Union[Unset, "Customer"] = UNSET
    discount: Union[None, Unset, str] = UNSET
    discount_type: Union[Unset, DocumentDiscountType] = UNSET
    document_date: Union[Unset, datetime.date] = UNSET
    due_date: Union[Unset, datetime.date] = UNSET
    """ To change the value use grace_period. """
    edited_at: Union[Unset, datetime.datetime] = UNSET
    external_id: Union[None, Unset, str] = UNSET
    replica_url: Union[None, Unset, str] = UNSET
    grace_period: Union[None, Unset, int] = UNSET
    """ will be replaced by its alias due_in_days. """
    due_in_days: Union[None, Unset, int] = UNSET
    """ due date in days. """
    id: Union[Unset, int] = UNSET
    is_acceptable_on_public_domain: Union[Unset, bool] = False
    """ Indicates if a document can be accepted by the end customer through the document's public access page. """
    is_archive: Union[Unset, bool] = False
    is_draft: Union[Unset, bool] = UNSET
    """ This property is read only. To finish the document call /documents/{id}/done. """
    is_replica: Union[Unset, bool] = False
    """ Marks a document as a replica from another software. """
    is_oss: Union[Unset, bool] = False
    """ Indicates if a document is a one-stop-shop document """
    item_notes: Union[Unset, list[str]] = UNSET
    """ Field holds all unique document_note of items for the document """
    items: Union[Unset, list["DocumentPosition"]] = UNSET
    last_postbox_id: Union[Unset, int] = UNSET
    login_id: Union[Unset, int] = UNSET
    """ If omitted or null, the currently active login is used. """
    number: Union[None, Unset, str] = UNSET
    order_number: Union[Unset, str] = ""
    buyer_reference: Union[Unset, str] = ""
    paid_amount: Union[Unset, int] = UNSET
    paid_at: Union[Unset, datetime.date] = UNSET
    pdf_pages: Union[Unset, int] = UNSET
    pdf_template: Union[Unset, str] = UNSET
    """ Default template is null or 'DE', default english is 'EN' and for all others use the numeric template ID.
    """
    project_id: Union[None, Unset, int] = UNSET
    recurring_options: Union[Unset, "DocumentRecurring"] = UNSET
    """ This object is only available in document type RECURRING. """
    ref_id: Union[None, Unset, int] = UNSET
    """ Reference document id """
    root_id: Union[None, Unset, int] = UNSET
    """ Root document id """
    service_date: Union[Unset, "ServiceDate"] = UNSET
    """ This object is only available in document type INVOICE or CREDIT. """
    shipping_country: Union[None, Unset, str] = UNSET
    status: Union[Unset, DocumentStatus] = UNSET
    """ This value can only be used in document type DELIVERY, ORDER, CHARGE or OFFER. NULL is default = not set.
    """
    text: Union[Unset, str] = UNSET
    text_prefix: Union[Unset, str] = UNSET
    text_tax: Union[None, Unset, str] = UNSET
    """ Overwrites the default vat-option text from the document layout. It is only displayed in documents with the
    type other than: Delivery, Dunning, Reminder or Letter and a different vat-option than null """
    title: Union[None, Unset, str] = UNSET
    type_: Union[Unset, DocumentType] = DocumentType.INVOICE
    """ Can only set on create. """
    use_shipping_address: Union[Unset, bool] = False
    """ If true and customer has shipping address then it will be used. """
    vat_country: Union[None, Unset, str] = UNSET
    vat_id: Union[Unset, str] = ""
    fulfillment_country: Union[None, Unset, str] = UNSET
    vat_option: Union[Unset, DocumentVatOption] = UNSET
    """ NULL: Normal steuerbar<br/> nStb: Nicht steuerbar (Drittland)<br/> nStbUstID: Nicht steuerbar (EU mit USt-
    IdNr.)<br/> nStbNoneUstID: Nicht steuerbar (EU ohne USt-IdNr.)<br/> nStbIm: Nicht steuerbarer Innenumsatz<br/>
    revc: Steuerschuldwechsel §13b (Inland)<br/> IG: Innergemeinschaftliche Lieferung<br/> AL: Ausfuhrlieferung<br/>
    sStfr: sonstige Steuerbefreiung<br/> smallBusiness: Kleinunternehmen (Keine MwSt.) """
    file_format_config: Union[Unset, list["FileFormatConfig"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        attachment_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.attachment_ids, Unset):
            attachment_ids = self.attachment_ids

        label_address: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.label_address, Unset):
            label_address = self.label_address.to_dict()

        amount = self.amount

        amount_net = self.amount_net

        anonymize_due_date: Union[None, Unset, str]
        if isinstance(self.anonymize_due_date, Unset):
            anonymize_due_date = UNSET
        elif isinstance(self.anonymize_due_date, datetime.date):
            anonymize_due_date = self.anonymize_due_date.isoformat()
        else:
            anonymize_due_date = self.anonymize_due_date

        anonymize_status: Union[Unset, str] = UNSET
        if not isinstance(self.anonymize_status, Unset):
            anonymize_status = self.anonymize_status.value

        anonymized_at: Union[None, Unset, str]
        if isinstance(self.anonymized_at, Unset):
            anonymized_at = UNSET
        else:
            anonymized_at = self.anonymized_at

        bank_debit_form: Union[None, Unset, str]
        if isinstance(self.bank_debit_form, Unset):
            bank_debit_form = UNSET
        else:
            bank_debit_form = self.bank_debit_form

        billing_country = self.billing_country

        calc_vat_from = self.calc_vat_from

        cancel_id = self.cancel_id

        cash_allowance: Union[None, Unset, float]
        if isinstance(self.cash_allowance, Unset):
            cash_allowance = UNSET
        else:
            cash_allowance = self.cash_allowance

        cash_allowance_days: Union[None, Unset, int]
        if isinstance(self.cash_allowance_days, Unset):
            cash_allowance_days = UNSET
        else:
            cash_allowance_days = self.cash_allowance_days

        cash_allowance_text: Union[None, Unset, str]
        if isinstance(self.cash_allowance_text, Unset):
            cash_allowance_text = UNSET
        else:
            cash_allowance_text = self.cash_allowance_text

        contact_id: Union[None, Unset, int]
        if isinstance(self.contact_id, Unset):
            contact_id = UNSET
        else:
            contact_id = self.contact_id

        contact_label = self.contact_label

        contact_text = self.contact_text

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        currency = self.currency

        customer_id: Union[None, Unset, int]
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        customer_snapshot: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.customer_snapshot, Unset):
            customer_snapshot = self.customer_snapshot.to_dict()

        discount: Union[None, Unset, str]
        if isinstance(self.discount, Unset):
            discount = UNSET
        else:
            discount = self.discount

        discount_type: Union[Unset, str] = UNSET
        if not isinstance(self.discount_type, Unset):
            discount_type = self.discount_type.value

        document_date: Union[Unset, str] = UNSET
        if not isinstance(self.document_date, Unset):
            document_date = self.document_date.isoformat()

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        edited_at: Union[Unset, str] = UNSET
        if not isinstance(self.edited_at, Unset):
            edited_at = self.edited_at.isoformat()

        external_id: Union[None, Unset, str]
        if isinstance(self.external_id, Unset):
            external_id = UNSET
        else:
            external_id = self.external_id

        replica_url: Union[None, Unset, str]
        if isinstance(self.replica_url, Unset):
            replica_url = UNSET
        else:
            replica_url = self.replica_url

        grace_period: Union[None, Unset, int]
        if isinstance(self.grace_period, Unset):
            grace_period = UNSET
        else:
            grace_period = self.grace_period

        due_in_days: Union[None, Unset, int]
        if isinstance(self.due_in_days, Unset):
            due_in_days = UNSET
        else:
            due_in_days = self.due_in_days

        id = self.id

        is_acceptable_on_public_domain = self.is_acceptable_on_public_domain

        is_archive = self.is_archive

        is_draft = self.is_draft

        is_replica = self.is_replica

        is_oss = self.is_oss

        item_notes: Union[Unset, list[str]] = UNSET
        if not isinstance(self.item_notes, Unset):
            item_notes = self.item_notes

        items: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()
                items.append(items_item)

        last_postbox_id = self.last_postbox_id

        login_id = self.login_id

        number: Union[None, Unset, str]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        order_number = self.order_number

        buyer_reference = self.buyer_reference

        paid_amount = self.paid_amount

        paid_at: Union[Unset, str] = UNSET
        if not isinstance(self.paid_at, Unset):
            paid_at = self.paid_at.isoformat()

        pdf_pages = self.pdf_pages

        pdf_template = self.pdf_template

        project_id: Union[None, Unset, int]
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        recurring_options: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.recurring_options, Unset):
            recurring_options = self.recurring_options.to_dict()

        ref_id: Union[None, Unset, int]
        if isinstance(self.ref_id, Unset):
            ref_id = UNSET
        else:
            ref_id = self.ref_id

        root_id: Union[None, Unset, int]
        if isinstance(self.root_id, Unset):
            root_id = UNSET
        else:
            root_id = self.root_id

        service_date: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.service_date, Unset):
            service_date = self.service_date.to_dict()

        shipping_country: Union[None, Unset, str]
        if isinstance(self.shipping_country, Unset):
            shipping_country = UNSET
        else:
            shipping_country = self.shipping_country

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        text = self.text

        text_prefix = self.text_prefix

        text_tax: Union[None, Unset, str]
        if isinstance(self.text_tax, Unset):
            text_tax = UNSET
        else:
            text_tax = self.text_tax

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        use_shipping_address = self.use_shipping_address

        vat_country: Union[None, Unset, str]
        if isinstance(self.vat_country, Unset):
            vat_country = UNSET
        else:
            vat_country = self.vat_country

        vat_id = self.vat_id

        fulfillment_country: Union[None, Unset, str]
        if isinstance(self.fulfillment_country, Unset):
            fulfillment_country = UNSET
        else:
            fulfillment_country = self.fulfillment_country

        vat_option: Union[Unset, str] = UNSET
        if not isinstance(self.vat_option, Unset):
            vat_option = self.vat_option.value

        file_format_config: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.file_format_config, Unset):
            file_format_config = []
            for file_format_config_item_data in self.file_format_config:
                file_format_config_item = file_format_config_item_data.to_dict()
                file_format_config.append(file_format_config_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address is not UNSET:
            field_dict["address"] = address
        if attachment_ids is not UNSET:
            field_dict["attachment_ids"] = attachment_ids
        if label_address is not UNSET:
            field_dict["label_address"] = label_address
        if amount is not UNSET:
            field_dict["amount"] = amount
        if amount_net is not UNSET:
            field_dict["amount_net"] = amount_net
        if anonymize_due_date is not UNSET:
            field_dict["anonymize_due_date"] = anonymize_due_date
        if anonymize_status is not UNSET:
            field_dict["anonymize_status"] = anonymize_status
        if anonymized_at is not UNSET:
            field_dict["anonymized_at"] = anonymized_at
        if bank_debit_form is not UNSET:
            field_dict["bank_debit_form"] = bank_debit_form
        if billing_country is not UNSET:
            field_dict["billing_country"] = billing_country
        if calc_vat_from is not UNSET:
            field_dict["calc_vat_from"] = calc_vat_from
        if cancel_id is not UNSET:
            field_dict["cancel_id"] = cancel_id
        if cash_allowance is not UNSET:
            field_dict["cash_allowance"] = cash_allowance
        if cash_allowance_days is not UNSET:
            field_dict["cash_allowance_days"] = cash_allowance_days
        if cash_allowance_text is not UNSET:
            field_dict["cash_allowance_text"] = cash_allowance_text
        if contact_id is not UNSET:
            field_dict["contact_id"] = contact_id
        if contact_label is not UNSET:
            field_dict["contact_label"] = contact_label
        if contact_text is not UNSET:
            field_dict["contact_text"] = contact_text
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if currency is not UNSET:
            field_dict["currency"] = currency
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if customer_snapshot is not UNSET:
            field_dict["customer_snapshot"] = customer_snapshot
        if discount is not UNSET:
            field_dict["discount"] = discount
        if discount_type is not UNSET:
            field_dict["discount_type"] = discount_type
        if document_date is not UNSET:
            field_dict["document_date"] = document_date
        if due_date is not UNSET:
            field_dict["due_date"] = due_date
        if edited_at is not UNSET:
            field_dict["edited_at"] = edited_at
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if replica_url is not UNSET:
            field_dict["replica_url"] = replica_url
        if grace_period is not UNSET:
            field_dict["grace_period"] = grace_period
        if due_in_days is not UNSET:
            field_dict["due_in_days"] = due_in_days
        if id is not UNSET:
            field_dict["id"] = id
        if is_acceptable_on_public_domain is not UNSET:
            field_dict["is_acceptable_on_public_domain"] = is_acceptable_on_public_domain
        if is_archive is not UNSET:
            field_dict["is_archive"] = is_archive
        if is_draft is not UNSET:
            field_dict["is_draft"] = is_draft
        if is_replica is not UNSET:
            field_dict["is_replica"] = is_replica
        if is_oss is not UNSET:
            field_dict["is_oss"] = is_oss
        if item_notes is not UNSET:
            field_dict["item_notes"] = item_notes
        if items is not UNSET:
            field_dict["items"] = items
        if last_postbox_id is not UNSET:
            field_dict["last_postbox_id"] = last_postbox_id
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if number is not UNSET:
            field_dict["number"] = number
        if order_number is not UNSET:
            field_dict["order_number"] = order_number
        if buyer_reference is not UNSET:
            field_dict["buyer_reference"] = buyer_reference
        if paid_amount is not UNSET:
            field_dict["paid_amount"] = paid_amount
        if paid_at is not UNSET:
            field_dict["paid_at"] = paid_at
        if pdf_pages is not UNSET:
            field_dict["pdf_pages"] = pdf_pages
        if pdf_template is not UNSET:
            field_dict["pdf_template"] = pdf_template
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if recurring_options is not UNSET:
            field_dict["recurring_options"] = recurring_options
        if ref_id is not UNSET:
            field_dict["ref_id"] = ref_id
        if root_id is not UNSET:
            field_dict["root_id"] = root_id
        if service_date is not UNSET:
            field_dict["service_date"] = service_date
        if shipping_country is not UNSET:
            field_dict["shipping_country"] = shipping_country
        if status is not UNSET:
            field_dict["status"] = status
        if text is not UNSET:
            field_dict["text"] = text
        if text_prefix is not UNSET:
            field_dict["text_prefix"] = text_prefix
        if text_tax is not UNSET:
            field_dict["text_tax"] = text_tax
        if title is not UNSET:
            field_dict["title"] = title
        if type_ is not UNSET:
            field_dict["type"] = type_
        if use_shipping_address is not UNSET:
            field_dict["use_shipping_address"] = use_shipping_address
        if vat_country is not UNSET:
            field_dict["vat_country"] = vat_country
        if vat_id is not UNSET:
            field_dict["vat_id"] = vat_id
        if fulfillment_country is not UNSET:
            field_dict["fulfillment_country"] = fulfillment_country
        if vat_option is not UNSET:
            field_dict["vat_option"] = vat_option
        if file_format_config is not UNSET:
            field_dict["file_format_config"] = file_format_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.customer import Customer
        from ..models.document_address import DocumentAddress
        from ..models.document_position import DocumentPosition
        from ..models.document_recurring import DocumentRecurring
        from ..models.file_format_config import FileFormatConfig
        from ..models.service_date import ServiceDate

        d = dict(src_dict)
        _address = d.pop("address", UNSET)
        address: Union[Unset, DocumentAddress]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = DocumentAddress.from_dict(_address)

        attachment_ids = cast(list[int], d.pop("attachment_ids", UNSET))

        _label_address = d.pop("label_address", UNSET)
        label_address: Union[Unset, DocumentAddress]
        if isinstance(_label_address, Unset):
            label_address = UNSET
        else:
            label_address = DocumentAddress.from_dict(_label_address)

        amount = d.pop("amount", UNSET)

        amount_net = d.pop("amount_net", UNSET)

        def _parse_anonymize_due_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                anonymize_due_date_type_0 = isoparse(data).date()

                return anonymize_due_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        anonymize_due_date = _parse_anonymize_due_date(d.pop("anonymize_due_date", UNSET))

        _anonymize_status = d.pop("anonymize_status", UNSET)
        anonymize_status: Union[Unset, DocumentAnonymizeStatus]
        if isinstance(_anonymize_status, Unset):
            anonymize_status = UNSET
        else:
            anonymize_status = DocumentAnonymizeStatus(_anonymize_status)

        def _parse_anonymized_at(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        anonymized_at = _parse_anonymized_at(d.pop("anonymized_at", UNSET))

        def _parse_bank_debit_form(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bank_debit_form = _parse_bank_debit_form(d.pop("bank_debit_form", UNSET))

        billing_country = d.pop("billing_country", UNSET)

        calc_vat_from = d.pop("calc_vat_from", UNSET)

        cancel_id = d.pop("cancel_id", UNSET)

        def _parse_cash_allowance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cash_allowance = _parse_cash_allowance(d.pop("cash_allowance", UNSET))

        def _parse_cash_allowance_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cash_allowance_days = _parse_cash_allowance_days(d.pop("cash_allowance_days", UNSET))

        def _parse_cash_allowance_text(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cash_allowance_text = _parse_cash_allowance_text(d.pop("cash_allowance_text", UNSET))

        def _parse_contact_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        contact_id = _parse_contact_id(d.pop("contact_id", UNSET))

        contact_label = d.pop("contact_label", UNSET)

        contact_text = d.pop("contact_text", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        currency = d.pop("currency", UNSET)

        def _parse_customer_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        _customer_snapshot = d.pop("customer_snapshot", UNSET)
        customer_snapshot: Union[Unset, Customer]
        if isinstance(_customer_snapshot, Unset):
            customer_snapshot = UNSET
        else:
            customer_snapshot = Customer.from_dict(_customer_snapshot)

        def _parse_discount(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        discount = _parse_discount(d.pop("discount", UNSET))

        _discount_type = d.pop("discount_type", UNSET)
        discount_type: Union[Unset, DocumentDiscountType]
        if isinstance(_discount_type, Unset):
            discount_type = UNSET
        else:
            discount_type = DocumentDiscountType(_discount_type)

        _document_date = d.pop("document_date", UNSET)
        document_date: Union[Unset, datetime.date]
        if isinstance(_document_date, Unset):
            document_date = UNSET
        else:
            document_date = isoparse(_document_date).date()

        _due_date = d.pop("due_date", UNSET)
        due_date: Union[Unset, datetime.date]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date).date()

        _edited_at = d.pop("edited_at", UNSET)
        edited_at: Union[Unset, datetime.datetime]
        if isinstance(_edited_at, Unset):
            edited_at = UNSET
        else:
            edited_at = isoparse(_edited_at)

        def _parse_external_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        external_id = _parse_external_id(d.pop("external_id", UNSET))

        def _parse_replica_url(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        replica_url = _parse_replica_url(d.pop("replica_url", UNSET))

        def _parse_grace_period(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        grace_period = _parse_grace_period(d.pop("grace_period", UNSET))

        def _parse_due_in_days(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        due_in_days = _parse_due_in_days(d.pop("due_in_days", UNSET))

        id = d.pop("id", UNSET)

        is_acceptable_on_public_domain = d.pop("is_acceptable_on_public_domain", UNSET)

        is_archive = d.pop("is_archive", UNSET)

        is_draft = d.pop("is_draft", UNSET)

        is_replica = d.pop("is_replica", UNSET)

        is_oss = d.pop("is_oss", UNSET)

        item_notes = cast(list[str], d.pop("item_notes", UNSET))

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = DocumentPosition.from_dict(items_item_data)

            items.append(items_item)

        last_postbox_id = d.pop("last_postbox_id", UNSET)

        login_id = d.pop("login_id", UNSET)

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))

        order_number = d.pop("order_number", UNSET)

        buyer_reference = d.pop("buyer_reference", UNSET)

        paid_amount = d.pop("paid_amount", UNSET)

        _paid_at = d.pop("paid_at", UNSET)
        paid_at: Union[Unset, datetime.date]
        if isinstance(_paid_at, Unset):
            paid_at = UNSET
        else:
            paid_at = isoparse(_paid_at).date()

        pdf_pages = d.pop("pdf_pages", UNSET)

        pdf_template = d.pop("pdf_template", UNSET)

        def _parse_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        _recurring_options = d.pop("recurring_options", UNSET)
        recurring_options: Union[Unset, DocumentRecurring]
        if isinstance(_recurring_options, Unset):
            recurring_options = UNSET
        else:
            recurring_options = DocumentRecurring.from_dict(_recurring_options)

        def _parse_ref_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        ref_id = _parse_ref_id(d.pop("ref_id", UNSET))

        def _parse_root_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        root_id = _parse_root_id(d.pop("root_id", UNSET))

        _service_date = d.pop("service_date", UNSET)
        service_date: Union[Unset, ServiceDate]
        if isinstance(_service_date, Unset):
            service_date = UNSET
        else:
            service_date = ServiceDate.from_dict(_service_date)

        def _parse_shipping_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        shipping_country = _parse_shipping_country(d.pop("shipping_country", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, DocumentStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DocumentStatus(_status)

        text = d.pop("text", UNSET)

        text_prefix = d.pop("text_prefix", UNSET)

        def _parse_text_tax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        text_tax = _parse_text_tax(d.pop("text_tax", UNSET))

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DocumentType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DocumentType(_type_)

        use_shipping_address = d.pop("use_shipping_address", UNSET)

        def _parse_vat_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vat_country = _parse_vat_country(d.pop("vat_country", UNSET))

        vat_id = d.pop("vat_id", UNSET)

        def _parse_fulfillment_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fulfillment_country = _parse_fulfillment_country(d.pop("fulfillment_country", UNSET))

        _vat_option = d.pop("vat_option", UNSET)
        vat_option: Union[Unset, DocumentVatOption]
        if isinstance(_vat_option, Unset):
            vat_option = UNSET
        else:
            vat_option = DocumentVatOption(_vat_option)

        file_format_config = []
        _file_format_config = d.pop("file_format_config", UNSET)
        for file_format_config_item_data in _file_format_config or []:
            file_format_config_item = FileFormatConfig.from_dict(file_format_config_item_data)

            file_format_config.append(file_format_config_item)

        document = cls(
            address=address,
            attachment_ids=attachment_ids,
            label_address=label_address,
            amount=amount,
            amount_net=amount_net,
            anonymize_due_date=anonymize_due_date,
            anonymize_status=anonymize_status,
            anonymized_at=anonymized_at,
            bank_debit_form=bank_debit_form,
            billing_country=billing_country,
            calc_vat_from=calc_vat_from,
            cancel_id=cancel_id,
            cash_allowance=cash_allowance,
            cash_allowance_days=cash_allowance_days,
            cash_allowance_text=cash_allowance_text,
            contact_id=contact_id,
            contact_label=contact_label,
            contact_text=contact_text,
            created_at=created_at,
            currency=currency,
            customer_id=customer_id,
            customer_snapshot=customer_snapshot,
            discount=discount,
            discount_type=discount_type,
            document_date=document_date,
            due_date=due_date,
            edited_at=edited_at,
            external_id=external_id,
            replica_url=replica_url,
            grace_period=grace_period,
            due_in_days=due_in_days,
            id=id,
            is_acceptable_on_public_domain=is_acceptable_on_public_domain,
            is_archive=is_archive,
            is_draft=is_draft,
            is_replica=is_replica,
            is_oss=is_oss,
            item_notes=item_notes,
            items=items,
            last_postbox_id=last_postbox_id,
            login_id=login_id,
            number=number,
            order_number=order_number,
            buyer_reference=buyer_reference,
            paid_amount=paid_amount,
            paid_at=paid_at,
            pdf_pages=pdf_pages,
            pdf_template=pdf_template,
            project_id=project_id,
            recurring_options=recurring_options,
            ref_id=ref_id,
            root_id=root_id,
            service_date=service_date,
            shipping_country=shipping_country,
            status=status,
            text=text,
            text_prefix=text_prefix,
            text_tax=text_tax,
            title=title,
            type_=type_,
            use_shipping_address=use_shipping_address,
            vat_country=vat_country,
            vat_id=vat_id,
            fulfillment_country=fulfillment_country,
            vat_option=vat_option,
            file_format_config=file_format_config,
        )

        document.additional_properties = d
        return document

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
