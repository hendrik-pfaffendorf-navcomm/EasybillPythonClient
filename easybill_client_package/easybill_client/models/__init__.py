"""Contains all the data models used in inputs/outputs"""

from .attachment import Attachment
from .attachments import Attachments
from .contact import Contact
from .contacts import Contacts
from .customer import Customer
from .customer_cash_discount_type import CustomerCashDiscountType
from .customer_document_pdf_type import CustomerDocumentPdfType
from .customer_group import CustomerGroup
from .customer_groups import CustomerGroups
from .customer_sale_price_level import CustomerSalePriceLevel
from .customer_sepa_agreement import CustomerSepaAgreement
from .customer_tax_options import CustomerTaxOptions
from .customers import Customers
from .discount import Discount
from .discount_discount_type import DiscountDiscountType
from .discount_position_groups import DiscountPositionGroups
from .discount_positions import DiscountPositions
from .document import Document
from .document_address import DocumentAddress
from .document_anonymize_status import DocumentAnonymizeStatus
from .document_discount_type import DocumentDiscountType
from .document_payment import DocumentPayment
from .document_payments import DocumentPayments
from .document_position import DocumentPosition
from .document_position_cost_price_charge_type import DocumentPositionCostPriceChargeType
from .document_position_discount_type import DocumentPositionDiscountType
from .document_position_item_type import DocumentPositionItemType
from .document_position_type import DocumentPositionType
from .document_recurring import DocumentRecurring
from .document_recurring_frequency import DocumentRecurringFrequency
from .document_recurring_frequency_special import DocumentRecurringFrequencySpecial
from .document_recurring_paid_date_option import DocumentRecurringPaidDateOption
from .document_recurring_send_as import DocumentRecurringSendAs
from .document_recurring_sepa_local_instrument import DocumentRecurringSepaLocalInstrument
from .document_recurring_sepa_sequence_type import DocumentRecurringSepaSequenceType
from .document_recurring_status import DocumentRecurringStatus
from .document_recurring_target_type import DocumentRecurringTargetType
from .document_status import DocumentStatus
from .document_type import DocumentType
from .document_vat_option import DocumentVatOption
from .document_version import DocumentVersion
from .document_version_item import DocumentVersionItem
from .document_version_item_document_version_item_type import DocumentVersionItemDocumentVersionItemType
from .document_versions import DocumentVersions
from .documents import Documents
from .file_format_config import FileFormatConfig
from .file_format_config_type import FileFormatConfigType
from .get_documents_is_archive import GetDocumentsIsArchive
from .get_documents_is_draft import GetDocumentsIsDraft
from .get_documents_type import GetDocumentsType
from .get_pdf_templates_type_item import GetPdfTemplatesTypeItem
from .get_positions_type import GetPositionsType
from .get_post_boxes_status import GetPostBoxesStatus
from .get_post_boxes_type import GetPostBoxesType
from .get_projects_status import GetProjectsStatus
from .list_ import List
from .login import Login
from .login_login_type import LoginLoginType
from .login_security import LoginSecurity
from .logins import Logins
from .pdf_template import PDFTemplate
from .pdf_template_settings import PDFTemplateSettings
from .pdf_template_settings_email import PDFTemplateSettingsEmail
from .pdf_templates import PDFTemplates
from .position import Position
from .position_export_identifier_extended import PositionExportIdentifierExtended
from .position_group import PositionGroup
from .position_groups import PositionGroups
from .position_price_type import PositionPriceType
from .position_stock import PositionStock
from .position_stock_limit_notify_frequency import PositionStockLimitNotifyFrequency
from .position_type import PositionType
from .positions import Positions
from .post_attachments_body import PostAttachmentsBody
from .post_box import PostBox
from .post_box_document_file_type import PostBoxDocumentFileType
from .post_box_post_send_type import PostBoxPostSendType
from .post_box_request import PostBoxRequest
from .post_box_request_document_file_type import PostBoxRequestDocumentFileType
from .post_box_request_post_send_type import PostBoxRequestPostSendType
from .post_box_status import PostBoxStatus
from .post_box_type import PostBoxType
from .post_boxes import PostBoxes
from .post_customers_type import PostCustomersType
from .post_documents_id_send_type_type import PostDocumentsIdSendTypeType
from .post_documents_id_type_type import PostDocumentsIdTypeType
from .project import Project
from .project_budget_notify_frequency import ProjectBudgetNotifyFrequency
from .project_status import ProjectStatus
from .projects import Projects
from .put_customers_id_type import PutCustomersIdType
from .sepa_payment import SEPAPayment
from .sepa_payment_local_instrument import SEPAPaymentLocalInstrument
from .sepa_payment_sequence_type import SEPAPaymentSequenceType
from .sepa_payment_type import SEPAPaymentType
from .sepa_payments import SEPAPayments
from .serial_number import SerialNumber
from .serial_numbers import SerialNumbers
from .service_date import ServiceDate
from .service_date_type import ServiceDateType
from .stock import Stock
from .stocks import Stocks
from .task import Task
from .task_category import TaskCategory
from .task_priority import TaskPriority
from .task_status import TaskStatus
from .tasks import Tasks
from .text_template import TextTemplate
from .text_templates import TextTemplates
from .time_tracking import TimeTracking
from .time_trackings import TimeTrackings
from .web_hook import WebHook
from .web_hook_content_type import WebHookContentType
from .web_hook_events_item import WebHookEventsItem
from .web_hook_last_response import WebHookLastResponse
from .web_hooks import WebHooks

__all__ = (
    "Attachment",
    "Attachments",
    "Contact",
    "Contacts",
    "Customer",
    "CustomerCashDiscountType",
    "CustomerDocumentPdfType",
    "CustomerGroup",
    "CustomerGroups",
    "Customers",
    "CustomerSalePriceLevel",
    "CustomerSepaAgreement",
    "CustomerTaxOptions",
    "Discount",
    "DiscountDiscountType",
    "DiscountPositionGroups",
    "DiscountPositions",
    "Document",
    "DocumentAddress",
    "DocumentAnonymizeStatus",
    "DocumentDiscountType",
    "DocumentPayment",
    "DocumentPayments",
    "DocumentPosition",
    "DocumentPositionCostPriceChargeType",
    "DocumentPositionDiscountType",
    "DocumentPositionItemType",
    "DocumentPositionType",
    "DocumentRecurring",
    "DocumentRecurringFrequency",
    "DocumentRecurringFrequencySpecial",
    "DocumentRecurringPaidDateOption",
    "DocumentRecurringSendAs",
    "DocumentRecurringSepaLocalInstrument",
    "DocumentRecurringSepaSequenceType",
    "DocumentRecurringStatus",
    "DocumentRecurringTargetType",
    "Documents",
    "DocumentStatus",
    "DocumentType",
    "DocumentVatOption",
    "DocumentVersion",
    "DocumentVersionItem",
    "DocumentVersionItemDocumentVersionItemType",
    "DocumentVersions",
    "FileFormatConfig",
    "FileFormatConfigType",
    "GetDocumentsIsArchive",
    "GetDocumentsIsDraft",
    "GetDocumentsType",
    "GetPdfTemplatesTypeItem",
    "GetPositionsType",
    "GetPostBoxesStatus",
    "GetPostBoxesType",
    "GetProjectsStatus",
    "List",
    "Login",
    "LoginLoginType",
    "Logins",
    "LoginSecurity",
    "PDFTemplate",
    "PDFTemplates",
    "PDFTemplateSettings",
    "PDFTemplateSettingsEmail",
    "Position",
    "PositionExportIdentifierExtended",
    "PositionGroup",
    "PositionGroups",
    "PositionPriceType",
    "Positions",
    "PositionStock",
    "PositionStockLimitNotifyFrequency",
    "PositionType",
    "PostAttachmentsBody",
    "PostBox",
    "PostBoxDocumentFileType",
    "PostBoxes",
    "PostBoxPostSendType",
    "PostBoxRequest",
    "PostBoxRequestDocumentFileType",
    "PostBoxRequestPostSendType",
    "PostBoxStatus",
    "PostBoxType",
    "PostCustomersType",
    "PostDocumentsIdSendTypeType",
    "PostDocumentsIdTypeType",
    "Project",
    "ProjectBudgetNotifyFrequency",
    "Projects",
    "ProjectStatus",
    "PutCustomersIdType",
    "SEPAPayment",
    "SEPAPaymentLocalInstrument",
    "SEPAPayments",
    "SEPAPaymentSequenceType",
    "SEPAPaymentType",
    "SerialNumber",
    "SerialNumbers",
    "ServiceDate",
    "ServiceDateType",
    "Stock",
    "Stocks",
    "Task",
    "TaskCategory",
    "TaskPriority",
    "Tasks",
    "TaskStatus",
    "TextTemplate",
    "TextTemplates",
    "TimeTracking",
    "TimeTrackings",
    "WebHook",
    "WebHookContentType",
    "WebHookEventsItem",
    "WebHookLastResponse",
    "WebHooks",
)
