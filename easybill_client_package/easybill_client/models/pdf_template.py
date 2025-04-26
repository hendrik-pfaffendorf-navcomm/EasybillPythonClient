from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pdf_template_settings import PDFTemplateSettings


T = TypeVar("T", bound="PDFTemplate")


@_attrs_define
class PDFTemplate:
    id: Union[Unset, str] = "INVOICE-DE"
    name: Union[Unset, str] = "Default template"
    pdf_template: Union[Unset, str] = "DE"
    document_type: Union[Unset, str] = "INVOICE"
    settings: Union[Unset, "PDFTemplateSettings"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        pdf_template = self.pdf_template

        document_type = self.document_type

        settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if pdf_template is not UNSET:
            field_dict["pdf_template"] = pdf_template
        if document_type is not UNSET:
            field_dict["document_type"] = document_type
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pdf_template_settings import PDFTemplateSettings

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        pdf_template = d.pop("pdf_template", UNSET)

        document_type = d.pop("document_type", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, PDFTemplateSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = PDFTemplateSettings.from_dict(_settings)

        pdf_template = cls(
            id=id,
            name=name,
            pdf_template=pdf_template,
            document_type=document_type,
            settings=settings,
        )

        pdf_template.additional_properties = d
        return pdf_template

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
