from enum import Enum


class WebHookEventsItem(str, Enum):
    CONTACT_CREATE = "contact.create"
    CONTACT_DELETE = "contact.delete"
    CONTACT_UPDATE = "contact.update"
    CUSTOMER_CREATE = "customer.create"
    CUSTOMER_DELETE = "customer.delete"
    CUSTOMER_UPDATE = "customer.update"
    DOCUMENT_COMPLETED = "document.completed"
    DOCUMENT_CREATE = "document.create"
    DOCUMENT_DELETED = "document.deleted"
    DOCUMENT_PAYMENT_ADD = "document.payment_add"
    DOCUMENT_PAYMENT_DELETE = "document.payment_delete"
    DOCUMENT_UPDATE = "document.update"
    POSITION_CREATE = "position.create"
    POSITION_DELETE = "position.delete"
    POSITION_UPDATE = "position.update"
    POSTBOX_CREATE = "postbox.create"
    POSTBOX_DELETE = "postbox.delete"
    POSTBOX_SENT = "postbox.sent"
    POSTBOX_UPDATE = "postbox.update"

    def __str__(self) -> str:
        return str(self.value)
