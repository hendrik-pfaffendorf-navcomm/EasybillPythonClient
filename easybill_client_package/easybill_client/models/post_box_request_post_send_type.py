from enum import Enum


class PostBoxRequestPostSendType(str, Enum):
    POST_SEND_TYPE_REGISTERED = "post_send_type_registered"
    POST_SEND_TYPE_REGISTERED_AND_PERSONAL = "post_send_type_registered_and_personal"
    POST_SEND_TYPE_REGISTERED_AND_RECEIPT = "post_send_type_registered_and_receipt"
    POST_SEND_TYPE_REGISTERED_THROWIN = "post_send_type_registered_throwin"
    POST_SEND_TYPE_STANDARD = "post_send_type_standard"

    def __str__(self) -> str:
        return str(self.value)
