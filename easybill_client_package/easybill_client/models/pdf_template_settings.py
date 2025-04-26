from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pdf_template_settings_email import PDFTemplateSettingsEmail


T = TypeVar("T", bound="PDFTemplateSettings")


@_attrs_define
class PDFTemplateSettings:
    text_prefix: Union[Unset, str] = ""
    text: Union[Unset, str] = ""
    email: Union[Unset, "PDFTemplateSettingsEmail"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        text_prefix = self.text_prefix

        text = self.text

        email: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if text_prefix is not UNSET:
            field_dict["text_prefix"] = text_prefix
        if text is not UNSET:
            field_dict["text"] = text
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pdf_template_settings_email import PDFTemplateSettingsEmail

        d = dict(src_dict)
        text_prefix = d.pop("text_prefix", UNSET)

        text = d.pop("text", UNSET)

        _email = d.pop("email", UNSET)
        email: Union[Unset, PDFTemplateSettingsEmail]
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = PDFTemplateSettingsEmail.from_dict(_email)

        pdf_template_settings = cls(
            text_prefix=text_prefix,
            text=text,
            email=email,
        )

        pdf_template_settings.additional_properties = d
        return pdf_template_settings

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
