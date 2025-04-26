import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.customer_cash_discount_type import CustomerCashDiscountType
from ..models.customer_document_pdf_type import CustomerDocumentPdfType
from ..models.customer_sale_price_level import CustomerSalePriceLevel
from ..models.customer_sepa_agreement import CustomerSepaAgreement
from ..models.customer_tax_options import CustomerTaxOptions
from ..types import UNSET, Unset

T = TypeVar("T", bound="Customer")


@_attrs_define
class Customer:
    company_name: Union[None, str]
    last_name: Union[None, str]
    acquire_options: Union[None, Unset, int] = UNSET
    """ 1 = Empfehlung eines anderen Kunden, 2 = Zeitungsanzeige, 3 = Eigene Akquisition, 4 = Mitarbeiter
    Akquisition, 5 = Google, 6 = Gelbe Seiten, 7 = Kostenlose Internet Plattform, 8 = Bezahlte Internet Plattform
    """
    additional_groups_ids: Union[Unset, list[int]] = UNSET
    bank_account: Union[None, Unset, str] = UNSET
    bank_account_owner: Union[None, Unset, str] = UNSET
    bank_bic: Union[None, Unset, str] = UNSET
    bank_code: Union[None, Unset, str] = UNSET
    bank_iban: Union[None, Unset, str] = UNSET
    bank_name: Union[None, Unset, str] = UNSET
    birth_date: Union[None, Unset, datetime.date] = UNSET
    cash_allowance: Union[None, Unset, float] = UNSET
    cash_allowance_days: Union[Unset, int] = UNSET
    cash_discount: Union[None, Unset, float] = UNSET
    cash_discount_type: Union[Unset, CustomerCashDiscountType] = UNSET
    city: Union[None, Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    created_at: Union[Unset, datetime.date] = UNSET
    updated_at: Union[Unset, str] = UNSET
    delivery_title: Union[Unset, str] = UNSET
    delivery_city: Union[None, Unset, str] = UNSET
    delivery_state: Union[Unset, str] = UNSET
    delivery_company_name: Union[None, Unset, str] = UNSET
    delivery_country: Union[None, Unset, str] = UNSET
    delivery_first_name: Union[None, Unset, str] = UNSET
    delivery_last_name: Union[None, Unset, str] = UNSET
    delivery_personal: Union[Unset, bool] = UNSET
    delivery_salutation: Union[Unset, int] = UNSET
    """ 0 = nothing, 1 = Mr, 2 = Mrs, 3 = Company, 4 = Mr & Mrs, 5 = Married couple, 6 = Family """
    delivery_street: Union[None, Unset, str] = UNSET
    delivery_suffix_1: Union[None, Unset, str] = UNSET
    delivery_suffix_2: Union[None, Unset, str] = UNSET
    delivery_zip_code: Union[None, Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    emails: Union[Unset, list[str]] = UNSET
    fax: Union[None, Unset, str] = UNSET
    first_name: Union[None, Unset, str] = UNSET
    grace_period: Union[None, Unset, int] = UNSET
    """ will be replaced by its alias due_in_days. """
    due_in_days: Union[None, Unset, int] = UNSET
    """ due date in days """
    group_id: Union[None, Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    info_1: Union[None, Unset, str] = UNSET
    info_2: Union[None, Unset, str] = UNSET
    internet: Union[None, Unset, str] = UNSET
    login_id: Union[Unset, int] = UNSET
    mobile: Union[None, Unset, str] = UNSET
    note: Union[None, Unset, str] = UNSET
    number: Union[Unset, str] = UNSET
    """ Automatically generated if empty/omitted and when no type in query is provided or the type 'CUSTOMER',
    'CUSTOMER,SUPPLIER' """
    supplier_number: Union[Unset, str] = UNSET
    """ Automatically generated if the type SUPPLIER or 'CUSTOMER,SUPPLIER' is provided as query parameter and the
    field supplier_number is empty/omitted. """
    payment_options: Union[None, Unset, int] = UNSET
    """ 1 = Stets pünktliche Zahlung, 2 = überwiegend pünktliche Zahlung, 3 = überwiegend verspätete Zahlung, 5 =
    Grundsätzlich verspätete Zahlung """
    personal: Union[Unset, bool] = False
    phone_1: Union[None, Unset, str] = UNSET
    phone_2: Union[None, Unset, str] = UNSET
    postbox: Union[None, Unset, str] = UNSET
    postbox_city: Union[None, Unset, str] = UNSET
    postbox_state: Union[Unset, str] = UNSET
    postbox_country: Union[None, Unset, str] = UNSET
    postbox_zip_code: Union[None, Unset, str] = UNSET
    sale_price_level: Union[Unset, CustomerSalePriceLevel] = UNSET
    salutation: Union[Unset, int] = UNSET
    """ 0 = nothing, 1 = Mr, 2 = Mrs, 3 = Company, 4 = Mr & Mrs, 5 = Married couple, 6 = Family """
    sepa_agreement: Union[Unset, CustomerSepaAgreement] = UNSET
    """ BASIC = SEPA-Basislastschrift, COR1 = SEPA-Basislastschrift COR1 (deprecated use BASIC instead), COMPANY =
    SEPA-Firmenlastschrift, NULL = Noch kein Mandat erteilt """
    sepa_agreement_date: Union[None, Unset, datetime.date] = UNSET
    sepa_mandate_reference: Union[None, Unset, str] = UNSET
    since_date: Union[None, Unset, datetime.date] = UNSET
    street: Union[None, Unset, str] = UNSET
    suffix_1: Union[None, Unset, str] = UNSET
    suffix_2: Union[None, Unset, str] = UNSET
    tax_number: Union[None, Unset, str] = UNSET
    court: Union[None, Unset, str] = UNSET
    court_registry_number: Union[None, Unset, str] = UNSET
    tax_options: Union[Unset, CustomerTaxOptions] = UNSET
    """ nStb = Nicht steuerbar (Drittland), nStbUstID = Nicht steuerbar (EU mit USt-IdNr.), nStbNoneUstID = Nicht
    steuerbar (EU ohne USt-IdNr.), revc = Steuerschuldwechsel §13b (Inland), IG = Innergemeinschaftliche Lieferung,
    AL = Ausfuhrlieferung, sStfr = sonstige Steuerbefreiung, NULL = Umsatzsteuerpflichtig """
    title: Union[None, Unset, str] = UNSET
    archived: Union[Unset, bool] = UNSET
    vat_identifier: Union[None, Unset, str] = UNSET
    zip_code: Union[None, Unset, str] = UNSET
    document_pdf_type: Union[Unset, CustomerDocumentPdfType] = CustomerDocumentPdfType.DEFAULT
    """ Type of PDF to use when sending a Document to the Customer. """
    buyer_reference: Union[Unset, str] = UNSET
    """ Used as "buyerReference" in ZUGFeRD and as "Leitweg-ID" in the XRechnung format. """
    foreign_supplier_number: Union[Unset, str] = UNSET
    """ The ID given to your company by the customer in his system. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        company_name: Union[None, str]
        company_name = self.company_name

        last_name: Union[None, str]
        last_name = self.last_name

        acquire_options: Union[None, Unset, int]
        if isinstance(self.acquire_options, Unset):
            acquire_options = UNSET
        else:
            acquire_options = self.acquire_options

        additional_groups_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.additional_groups_ids, Unset):
            additional_groups_ids = self.additional_groups_ids

        bank_account: Union[None, Unset, str]
        if isinstance(self.bank_account, Unset):
            bank_account = UNSET
        else:
            bank_account = self.bank_account

        bank_account_owner: Union[None, Unset, str]
        if isinstance(self.bank_account_owner, Unset):
            bank_account_owner = UNSET
        else:
            bank_account_owner = self.bank_account_owner

        bank_bic: Union[None, Unset, str]
        if isinstance(self.bank_bic, Unset):
            bank_bic = UNSET
        else:
            bank_bic = self.bank_bic

        bank_code: Union[None, Unset, str]
        if isinstance(self.bank_code, Unset):
            bank_code = UNSET
        else:
            bank_code = self.bank_code

        bank_iban: Union[None, Unset, str]
        if isinstance(self.bank_iban, Unset):
            bank_iban = UNSET
        else:
            bank_iban = self.bank_iban

        bank_name: Union[None, Unset, str]
        if isinstance(self.bank_name, Unset):
            bank_name = UNSET
        else:
            bank_name = self.bank_name

        birth_date: Union[None, Unset, str]
        if isinstance(self.birth_date, Unset):
            birth_date = UNSET
        elif isinstance(self.birth_date, datetime.date):
            birth_date = self.birth_date.isoformat()
        else:
            birth_date = self.birth_date

        cash_allowance: Union[None, Unset, float]
        if isinstance(self.cash_allowance, Unset):
            cash_allowance = UNSET
        else:
            cash_allowance = self.cash_allowance

        cash_allowance_days = self.cash_allowance_days

        cash_discount: Union[None, Unset, float]
        if isinstance(self.cash_discount, Unset):
            cash_discount = UNSET
        else:
            cash_discount = self.cash_discount

        cash_discount_type: Union[Unset, str] = UNSET
        if not isinstance(self.cash_discount_type, Unset):
            cash_discount_type = self.cash_discount_type.value

        city: Union[None, Unset, str]
        if isinstance(self.city, Unset):
            city = UNSET
        else:
            city = self.city

        state = self.state

        country = self.country

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        updated_at = self.updated_at

        delivery_title = self.delivery_title

        delivery_city: Union[None, Unset, str]
        if isinstance(self.delivery_city, Unset):
            delivery_city = UNSET
        else:
            delivery_city = self.delivery_city

        delivery_state = self.delivery_state

        delivery_company_name: Union[None, Unset, str]
        if isinstance(self.delivery_company_name, Unset):
            delivery_company_name = UNSET
        else:
            delivery_company_name = self.delivery_company_name

        delivery_country: Union[None, Unset, str]
        if isinstance(self.delivery_country, Unset):
            delivery_country = UNSET
        else:
            delivery_country = self.delivery_country

        delivery_first_name: Union[None, Unset, str]
        if isinstance(self.delivery_first_name, Unset):
            delivery_first_name = UNSET
        else:
            delivery_first_name = self.delivery_first_name

        delivery_last_name: Union[None, Unset, str]
        if isinstance(self.delivery_last_name, Unset):
            delivery_last_name = UNSET
        else:
            delivery_last_name = self.delivery_last_name

        delivery_personal = self.delivery_personal

        delivery_salutation = self.delivery_salutation

        delivery_street: Union[None, Unset, str]
        if isinstance(self.delivery_street, Unset):
            delivery_street = UNSET
        else:
            delivery_street = self.delivery_street

        delivery_suffix_1: Union[None, Unset, str]
        if isinstance(self.delivery_suffix_1, Unset):
            delivery_suffix_1 = UNSET
        else:
            delivery_suffix_1 = self.delivery_suffix_1

        delivery_suffix_2: Union[None, Unset, str]
        if isinstance(self.delivery_suffix_2, Unset):
            delivery_suffix_2 = UNSET
        else:
            delivery_suffix_2 = self.delivery_suffix_2

        delivery_zip_code: Union[None, Unset, str]
        if isinstance(self.delivery_zip_code, Unset):
            delivery_zip_code = UNSET
        else:
            delivery_zip_code = self.delivery_zip_code

        display_name = self.display_name

        emails: Union[Unset, list[str]] = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        fax: Union[None, Unset, str]
        if isinstance(self.fax, Unset):
            fax = UNSET
        else:
            fax = self.fax

        first_name: Union[None, Unset, str]
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

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

        group_id: Union[None, Unset, int]
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        id = self.id

        info_1: Union[None, Unset, str]
        if isinstance(self.info_1, Unset):
            info_1 = UNSET
        else:
            info_1 = self.info_1

        info_2: Union[None, Unset, str]
        if isinstance(self.info_2, Unset):
            info_2 = UNSET
        else:
            info_2 = self.info_2

        internet: Union[None, Unset, str]
        if isinstance(self.internet, Unset):
            internet = UNSET
        else:
            internet = self.internet

        login_id = self.login_id

        mobile: Union[None, Unset, str]
        if isinstance(self.mobile, Unset):
            mobile = UNSET
        else:
            mobile = self.mobile

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        number = self.number

        supplier_number = self.supplier_number

        payment_options: Union[None, Unset, int]
        if isinstance(self.payment_options, Unset):
            payment_options = UNSET
        else:
            payment_options = self.payment_options

        personal = self.personal

        phone_1: Union[None, Unset, str]
        if isinstance(self.phone_1, Unset):
            phone_1 = UNSET
        else:
            phone_1 = self.phone_1

        phone_2: Union[None, Unset, str]
        if isinstance(self.phone_2, Unset):
            phone_2 = UNSET
        else:
            phone_2 = self.phone_2

        postbox: Union[None, Unset, str]
        if isinstance(self.postbox, Unset):
            postbox = UNSET
        else:
            postbox = self.postbox

        postbox_city: Union[None, Unset, str]
        if isinstance(self.postbox_city, Unset):
            postbox_city = UNSET
        else:
            postbox_city = self.postbox_city

        postbox_state = self.postbox_state

        postbox_country: Union[None, Unset, str]
        if isinstance(self.postbox_country, Unset):
            postbox_country = UNSET
        else:
            postbox_country = self.postbox_country

        postbox_zip_code: Union[None, Unset, str]
        if isinstance(self.postbox_zip_code, Unset):
            postbox_zip_code = UNSET
        else:
            postbox_zip_code = self.postbox_zip_code

        sale_price_level: Union[Unset, str] = UNSET
        if not isinstance(self.sale_price_level, Unset):
            sale_price_level = self.sale_price_level.value

        salutation = self.salutation

        sepa_agreement: Union[Unset, str] = UNSET
        if not isinstance(self.sepa_agreement, Unset):
            sepa_agreement = self.sepa_agreement.value

        sepa_agreement_date: Union[None, Unset, str]
        if isinstance(self.sepa_agreement_date, Unset):
            sepa_agreement_date = UNSET
        elif isinstance(self.sepa_agreement_date, datetime.date):
            sepa_agreement_date = self.sepa_agreement_date.isoformat()
        else:
            sepa_agreement_date = self.sepa_agreement_date

        sepa_mandate_reference: Union[None, Unset, str]
        if isinstance(self.sepa_mandate_reference, Unset):
            sepa_mandate_reference = UNSET
        else:
            sepa_mandate_reference = self.sepa_mandate_reference

        since_date: Union[None, Unset, str]
        if isinstance(self.since_date, Unset):
            since_date = UNSET
        elif isinstance(self.since_date, datetime.date):
            since_date = self.since_date.isoformat()
        else:
            since_date = self.since_date

        street: Union[None, Unset, str]
        if isinstance(self.street, Unset):
            street = UNSET
        else:
            street = self.street

        suffix_1: Union[None, Unset, str]
        if isinstance(self.suffix_1, Unset):
            suffix_1 = UNSET
        else:
            suffix_1 = self.suffix_1

        suffix_2: Union[None, Unset, str]
        if isinstance(self.suffix_2, Unset):
            suffix_2 = UNSET
        else:
            suffix_2 = self.suffix_2

        tax_number: Union[None, Unset, str]
        if isinstance(self.tax_number, Unset):
            tax_number = UNSET
        else:
            tax_number = self.tax_number

        court: Union[None, Unset, str]
        if isinstance(self.court, Unset):
            court = UNSET
        else:
            court = self.court

        court_registry_number: Union[None, Unset, str]
        if isinstance(self.court_registry_number, Unset):
            court_registry_number = UNSET
        else:
            court_registry_number = self.court_registry_number

        tax_options: Union[Unset, str] = UNSET
        if not isinstance(self.tax_options, Unset):
            tax_options = self.tax_options.value

        title: Union[None, Unset, str]
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        archived = self.archived

        vat_identifier: Union[None, Unset, str]
        if isinstance(self.vat_identifier, Unset):
            vat_identifier = UNSET
        else:
            vat_identifier = self.vat_identifier

        zip_code: Union[None, Unset, str]
        if isinstance(self.zip_code, Unset):
            zip_code = UNSET
        else:
            zip_code = self.zip_code

        document_pdf_type: Union[Unset, str] = UNSET
        if not isinstance(self.document_pdf_type, Unset):
            document_pdf_type = self.document_pdf_type.value

        buyer_reference = self.buyer_reference

        foreign_supplier_number = self.foreign_supplier_number

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "company_name": company_name,
                "last_name": last_name,
            }
        )
        if acquire_options is not UNSET:
            field_dict["acquire_options"] = acquire_options
        if additional_groups_ids is not UNSET:
            field_dict["additional_groups_ids"] = additional_groups_ids
        if bank_account is not UNSET:
            field_dict["bank_account"] = bank_account
        if bank_account_owner is not UNSET:
            field_dict["bank_account_owner"] = bank_account_owner
        if bank_bic is not UNSET:
            field_dict["bank_bic"] = bank_bic
        if bank_code is not UNSET:
            field_dict["bank_code"] = bank_code
        if bank_iban is not UNSET:
            field_dict["bank_iban"] = bank_iban
        if bank_name is not UNSET:
            field_dict["bank_name"] = bank_name
        if birth_date is not UNSET:
            field_dict["birth_date"] = birth_date
        if cash_allowance is not UNSET:
            field_dict["cash_allowance"] = cash_allowance
        if cash_allowance_days is not UNSET:
            field_dict["cash_allowance_days"] = cash_allowance_days
        if cash_discount is not UNSET:
            field_dict["cash_discount"] = cash_discount
        if cash_discount_type is not UNSET:
            field_dict["cash_discount_type"] = cash_discount_type
        if city is not UNSET:
            field_dict["city"] = city
        if state is not UNSET:
            field_dict["state"] = state
        if country is not UNSET:
            field_dict["country"] = country
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if updated_at is not UNSET:
            field_dict["updated_at"] = updated_at
        if delivery_title is not UNSET:
            field_dict["delivery_title"] = delivery_title
        if delivery_city is not UNSET:
            field_dict["delivery_city"] = delivery_city
        if delivery_state is not UNSET:
            field_dict["delivery_state"] = delivery_state
        if delivery_company_name is not UNSET:
            field_dict["delivery_company_name"] = delivery_company_name
        if delivery_country is not UNSET:
            field_dict["delivery_country"] = delivery_country
        if delivery_first_name is not UNSET:
            field_dict["delivery_first_name"] = delivery_first_name
        if delivery_last_name is not UNSET:
            field_dict["delivery_last_name"] = delivery_last_name
        if delivery_personal is not UNSET:
            field_dict["delivery_personal"] = delivery_personal
        if delivery_salutation is not UNSET:
            field_dict["delivery_salutation"] = delivery_salutation
        if delivery_street is not UNSET:
            field_dict["delivery_street"] = delivery_street
        if delivery_suffix_1 is not UNSET:
            field_dict["delivery_suffix_1"] = delivery_suffix_1
        if delivery_suffix_2 is not UNSET:
            field_dict["delivery_suffix_2"] = delivery_suffix_2
        if delivery_zip_code is not UNSET:
            field_dict["delivery_zip_code"] = delivery_zip_code
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if emails is not UNSET:
            field_dict["emails"] = emails
        if fax is not UNSET:
            field_dict["fax"] = fax
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if grace_period is not UNSET:
            field_dict["grace_period"] = grace_period
        if due_in_days is not UNSET:
            field_dict["due_in_days"] = due_in_days
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if id is not UNSET:
            field_dict["id"] = id
        if info_1 is not UNSET:
            field_dict["info_1"] = info_1
        if info_2 is not UNSET:
            field_dict["info_2"] = info_2
        if internet is not UNSET:
            field_dict["internet"] = internet
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if mobile is not UNSET:
            field_dict["mobile"] = mobile
        if note is not UNSET:
            field_dict["note"] = note
        if number is not UNSET:
            field_dict["number"] = number
        if supplier_number is not UNSET:
            field_dict["supplier_number"] = supplier_number
        if payment_options is not UNSET:
            field_dict["payment_options"] = payment_options
        if personal is not UNSET:
            field_dict["personal"] = personal
        if phone_1 is not UNSET:
            field_dict["phone_1"] = phone_1
        if phone_2 is not UNSET:
            field_dict["phone_2"] = phone_2
        if postbox is not UNSET:
            field_dict["postbox"] = postbox
        if postbox_city is not UNSET:
            field_dict["postbox_city"] = postbox_city
        if postbox_state is not UNSET:
            field_dict["postbox_state"] = postbox_state
        if postbox_country is not UNSET:
            field_dict["postbox_country"] = postbox_country
        if postbox_zip_code is not UNSET:
            field_dict["postbox_zip_code"] = postbox_zip_code
        if sale_price_level is not UNSET:
            field_dict["sale_price_level"] = sale_price_level
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if sepa_agreement is not UNSET:
            field_dict["sepa_agreement"] = sepa_agreement
        if sepa_agreement_date is not UNSET:
            field_dict["sepa_agreement_date"] = sepa_agreement_date
        if sepa_mandate_reference is not UNSET:
            field_dict["sepa_mandate_reference"] = sepa_mandate_reference
        if since_date is not UNSET:
            field_dict["since_date"] = since_date
        if street is not UNSET:
            field_dict["street"] = street
        if suffix_1 is not UNSET:
            field_dict["suffix_1"] = suffix_1
        if suffix_2 is not UNSET:
            field_dict["suffix_2"] = suffix_2
        if tax_number is not UNSET:
            field_dict["tax_number"] = tax_number
        if court is not UNSET:
            field_dict["court"] = court
        if court_registry_number is not UNSET:
            field_dict["court_registry_number"] = court_registry_number
        if tax_options is not UNSET:
            field_dict["tax_options"] = tax_options
        if title is not UNSET:
            field_dict["title"] = title
        if archived is not UNSET:
            field_dict["archived"] = archived
        if vat_identifier is not UNSET:
            field_dict["vat_identifier"] = vat_identifier
        if zip_code is not UNSET:
            field_dict["zip_code"] = zip_code
        if document_pdf_type is not UNSET:
            field_dict["document_pdf_type"] = document_pdf_type
        if buyer_reference is not UNSET:
            field_dict["buyer_reference"] = buyer_reference
        if foreign_supplier_number is not UNSET:
            field_dict["foreign_supplier_number"] = foreign_supplier_number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_company_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        company_name = _parse_company_name(d.pop("company_name"))

        def _parse_last_name(data: object) -> Union[None, str]:
            if data is None:
                return data
            return cast(Union[None, str], data)

        last_name = _parse_last_name(d.pop("last_name"))

        def _parse_acquire_options(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        acquire_options = _parse_acquire_options(d.pop("acquire_options", UNSET))

        additional_groups_ids = cast(list[int], d.pop("additional_groups_ids", UNSET))

        def _parse_bank_account(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bank_account = _parse_bank_account(d.pop("bank_account", UNSET))

        def _parse_bank_account_owner(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bank_account_owner = _parse_bank_account_owner(d.pop("bank_account_owner", UNSET))

        def _parse_bank_bic(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bank_bic = _parse_bank_bic(d.pop("bank_bic", UNSET))

        def _parse_bank_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bank_code = _parse_bank_code(d.pop("bank_code", UNSET))

        def _parse_bank_iban(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bank_iban = _parse_bank_iban(d.pop("bank_iban", UNSET))

        def _parse_bank_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        bank_name = _parse_bank_name(d.pop("bank_name", UNSET))

        def _parse_birth_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                birth_date_type_0 = isoparse(data).date()

                return birth_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        birth_date = _parse_birth_date(d.pop("birth_date", UNSET))

        def _parse_cash_allowance(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cash_allowance = _parse_cash_allowance(d.pop("cash_allowance", UNSET))

        cash_allowance_days = d.pop("cash_allowance_days", UNSET)

        def _parse_cash_discount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cash_discount = _parse_cash_discount(d.pop("cash_discount", UNSET))

        _cash_discount_type = d.pop("cash_discount_type", UNSET)
        cash_discount_type: Union[Unset, CustomerCashDiscountType]
        if isinstance(_cash_discount_type, Unset):
            cash_discount_type = UNSET
        else:
            cash_discount_type = CustomerCashDiscountType(_cash_discount_type)

        def _parse_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        city = _parse_city(d.pop("city", UNSET))

        state = d.pop("state", UNSET)

        country = d.pop("country", UNSET)

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.date]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at).date()

        updated_at = d.pop("updated_at", UNSET)

        delivery_title = d.pop("delivery_title", UNSET)

        def _parse_delivery_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_city = _parse_delivery_city(d.pop("delivery_city", UNSET))

        delivery_state = d.pop("delivery_state", UNSET)

        def _parse_delivery_company_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_company_name = _parse_delivery_company_name(d.pop("delivery_company_name", UNSET))

        def _parse_delivery_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_country = _parse_delivery_country(d.pop("delivery_country", UNSET))

        def _parse_delivery_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_first_name = _parse_delivery_first_name(d.pop("delivery_first_name", UNSET))

        def _parse_delivery_last_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_last_name = _parse_delivery_last_name(d.pop("delivery_last_name", UNSET))

        delivery_personal = d.pop("delivery_personal", UNSET)

        delivery_salutation = d.pop("delivery_salutation", UNSET)

        def _parse_delivery_street(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_street = _parse_delivery_street(d.pop("delivery_street", UNSET))

        def _parse_delivery_suffix_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_suffix_1 = _parse_delivery_suffix_1(d.pop("delivery_suffix_1", UNSET))

        def _parse_delivery_suffix_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_suffix_2 = _parse_delivery_suffix_2(d.pop("delivery_suffix_2", UNSET))

        def _parse_delivery_zip_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        delivery_zip_code = _parse_delivery_zip_code(d.pop("delivery_zip_code", UNSET))

        display_name = d.pop("display_name", UNSET)

        emails = cast(list[str], d.pop("emails", UNSET))

        def _parse_fax(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        fax = _parse_fax(d.pop("fax", UNSET))

        def _parse_first_name(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))

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

        def _parse_group_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        id = d.pop("id", UNSET)

        def _parse_info_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        info_1 = _parse_info_1(d.pop("info_1", UNSET))

        def _parse_info_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        info_2 = _parse_info_2(d.pop("info_2", UNSET))

        def _parse_internet(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        internet = _parse_internet(d.pop("internet", UNSET))

        login_id = d.pop("login_id", UNSET)

        def _parse_mobile(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        mobile = _parse_mobile(d.pop("mobile", UNSET))

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        number = d.pop("number", UNSET)

        supplier_number = d.pop("supplier_number", UNSET)

        def _parse_payment_options(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        payment_options = _parse_payment_options(d.pop("payment_options", UNSET))

        personal = d.pop("personal", UNSET)

        def _parse_phone_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_1 = _parse_phone_1(d.pop("phone_1", UNSET))

        def _parse_phone_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        phone_2 = _parse_phone_2(d.pop("phone_2", UNSET))

        def _parse_postbox(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postbox = _parse_postbox(d.pop("postbox", UNSET))

        def _parse_postbox_city(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postbox_city = _parse_postbox_city(d.pop("postbox_city", UNSET))

        postbox_state = d.pop("postbox_state", UNSET)

        def _parse_postbox_country(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postbox_country = _parse_postbox_country(d.pop("postbox_country", UNSET))

        def _parse_postbox_zip_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        postbox_zip_code = _parse_postbox_zip_code(d.pop("postbox_zip_code", UNSET))

        _sale_price_level = d.pop("sale_price_level", UNSET)
        sale_price_level: Union[Unset, CustomerSalePriceLevel]
        if isinstance(_sale_price_level, Unset):
            sale_price_level = UNSET
        else:
            sale_price_level = CustomerSalePriceLevel(_sale_price_level)

        salutation = d.pop("salutation", UNSET)

        _sepa_agreement = d.pop("sepa_agreement", UNSET)
        sepa_agreement: Union[Unset, CustomerSepaAgreement]
        if isinstance(_sepa_agreement, Unset):
            sepa_agreement = UNSET
        else:
            sepa_agreement = CustomerSepaAgreement(_sepa_agreement)

        def _parse_sepa_agreement_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sepa_agreement_date_type_0 = isoparse(data).date()

                return sepa_agreement_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        sepa_agreement_date = _parse_sepa_agreement_date(d.pop("sepa_agreement_date", UNSET))

        def _parse_sepa_mandate_reference(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        sepa_mandate_reference = _parse_sepa_mandate_reference(d.pop("sepa_mandate_reference", UNSET))

        def _parse_since_date(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                since_date_type_0 = isoparse(data).date()

                return since_date_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        since_date = _parse_since_date(d.pop("since_date", UNSET))

        def _parse_street(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        street = _parse_street(d.pop("street", UNSET))

        def _parse_suffix_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suffix_1 = _parse_suffix_1(d.pop("suffix_1", UNSET))

        def _parse_suffix_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        suffix_2 = _parse_suffix_2(d.pop("suffix_2", UNSET))

        def _parse_tax_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        tax_number = _parse_tax_number(d.pop("tax_number", UNSET))

        def _parse_court(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        court = _parse_court(d.pop("court", UNSET))

        def _parse_court_registry_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        court_registry_number = _parse_court_registry_number(d.pop("court_registry_number", UNSET))

        _tax_options = d.pop("tax_options", UNSET)
        tax_options: Union[Unset, CustomerTaxOptions]
        if isinstance(_tax_options, Unset):
            tax_options = UNSET
        else:
            tax_options = CustomerTaxOptions(_tax_options)

        def _parse_title(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        title = _parse_title(d.pop("title", UNSET))

        archived = d.pop("archived", UNSET)

        def _parse_vat_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        vat_identifier = _parse_vat_identifier(d.pop("vat_identifier", UNSET))

        def _parse_zip_code(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        zip_code = _parse_zip_code(d.pop("zip_code", UNSET))

        _document_pdf_type = d.pop("document_pdf_type", UNSET)
        document_pdf_type: Union[Unset, CustomerDocumentPdfType]
        if isinstance(_document_pdf_type, Unset):
            document_pdf_type = UNSET
        else:
            document_pdf_type = CustomerDocumentPdfType(_document_pdf_type)

        buyer_reference = d.pop("buyer_reference", UNSET)

        foreign_supplier_number = d.pop("foreign_supplier_number", UNSET)

        customer = cls(
            company_name=company_name,
            last_name=last_name,
            acquire_options=acquire_options,
            additional_groups_ids=additional_groups_ids,
            bank_account=bank_account,
            bank_account_owner=bank_account_owner,
            bank_bic=bank_bic,
            bank_code=bank_code,
            bank_iban=bank_iban,
            bank_name=bank_name,
            birth_date=birth_date,
            cash_allowance=cash_allowance,
            cash_allowance_days=cash_allowance_days,
            cash_discount=cash_discount,
            cash_discount_type=cash_discount_type,
            city=city,
            state=state,
            country=country,
            created_at=created_at,
            updated_at=updated_at,
            delivery_title=delivery_title,
            delivery_city=delivery_city,
            delivery_state=delivery_state,
            delivery_company_name=delivery_company_name,
            delivery_country=delivery_country,
            delivery_first_name=delivery_first_name,
            delivery_last_name=delivery_last_name,
            delivery_personal=delivery_personal,
            delivery_salutation=delivery_salutation,
            delivery_street=delivery_street,
            delivery_suffix_1=delivery_suffix_1,
            delivery_suffix_2=delivery_suffix_2,
            delivery_zip_code=delivery_zip_code,
            display_name=display_name,
            emails=emails,
            fax=fax,
            first_name=first_name,
            grace_period=grace_period,
            due_in_days=due_in_days,
            group_id=group_id,
            id=id,
            info_1=info_1,
            info_2=info_2,
            internet=internet,
            login_id=login_id,
            mobile=mobile,
            note=note,
            number=number,
            supplier_number=supplier_number,
            payment_options=payment_options,
            personal=personal,
            phone_1=phone_1,
            phone_2=phone_2,
            postbox=postbox,
            postbox_city=postbox_city,
            postbox_state=postbox_state,
            postbox_country=postbox_country,
            postbox_zip_code=postbox_zip_code,
            sale_price_level=sale_price_level,
            salutation=salutation,
            sepa_agreement=sepa_agreement,
            sepa_agreement_date=sepa_agreement_date,
            sepa_mandate_reference=sepa_mandate_reference,
            since_date=since_date,
            street=street,
            suffix_1=suffix_1,
            suffix_2=suffix_2,
            tax_number=tax_number,
            court=court,
            court_registry_number=court_registry_number,
            tax_options=tax_options,
            title=title,
            archived=archived,
            vat_identifier=vat_identifier,
            zip_code=zip_code,
            document_pdf_type=document_pdf_type,
            buyer_reference=buyer_reference,
            foreign_supplier_number=foreign_supplier_number,
        )

        customer.additional_properties = d
        return customer

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
