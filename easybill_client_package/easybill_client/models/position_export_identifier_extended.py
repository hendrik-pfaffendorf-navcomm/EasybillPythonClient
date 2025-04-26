from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PositionExportIdentifierExtended")


@_attrs_define
class PositionExportIdentifierExtended:
    null: Union[None, Unset, str] = UNSET
    """ Umsatzsteuerpflichtig """
    n_stb: Union[None, Unset, str] = UNSET
    """ Nicht steuerbar (Drittland) """
    n_stb_ust_id: Union[None, Unset, str] = UNSET
    """ Nicht steuerbar (EU mit USt-IdNr.) """
    n_stb_none_ust_id: Union[None, Unset, str] = UNSET
    """ Nicht steuerbar (EU ohne USt-IdNr.) """
    n_stb_im: Union[None, Unset, str] = UNSET
    """ Nicht steuerbarer Innenumsatz """
    revc: Union[None, Unset, str] = UNSET
    """ Steuerschuldwechsel §13b (Inland) """
    ig: Union[None, Unset, str] = UNSET
    """ Innergemeinschaftliche Lieferung """
    al: Union[None, Unset, str] = UNSET
    """ Ausfuhrlieferung """
    s_stfr: Union[None, Unset, str] = UNSET
    """ sonstige Steuerbefreiung """
    small_business: Union[None, Unset, str] = UNSET
    """ Kleinunternehmen (Keine MwSt.) """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        null: Union[None, Unset, str]
        if isinstance(self.null, Unset):
            null = UNSET
        else:
            null = self.null

        n_stb: Union[None, Unset, str]
        if isinstance(self.n_stb, Unset):
            n_stb = UNSET
        else:
            n_stb = self.n_stb

        n_stb_ust_id: Union[None, Unset, str]
        if isinstance(self.n_stb_ust_id, Unset):
            n_stb_ust_id = UNSET
        else:
            n_stb_ust_id = self.n_stb_ust_id

        n_stb_none_ust_id: Union[None, Unset, str]
        if isinstance(self.n_stb_none_ust_id, Unset):
            n_stb_none_ust_id = UNSET
        else:
            n_stb_none_ust_id = self.n_stb_none_ust_id

        n_stb_im: Union[None, Unset, str]
        if isinstance(self.n_stb_im, Unset):
            n_stb_im = UNSET
        else:
            n_stb_im = self.n_stb_im

        revc: Union[None, Unset, str]
        if isinstance(self.revc, Unset):
            revc = UNSET
        else:
            revc = self.revc

        ig: Union[None, Unset, str]
        if isinstance(self.ig, Unset):
            ig = UNSET
        else:
            ig = self.ig

        al: Union[None, Unset, str]
        if isinstance(self.al, Unset):
            al = UNSET
        else:
            al = self.al

        s_stfr: Union[None, Unset, str]
        if isinstance(self.s_stfr, Unset):
            s_stfr = UNSET
        else:
            s_stfr = self.s_stfr

        small_business: Union[None, Unset, str]
        if isinstance(self.small_business, Unset):
            small_business = UNSET
        else:
            small_business = self.small_business

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if null is not UNSET:
            field_dict["NULL"] = null
        if n_stb is not UNSET:
            field_dict["nStb"] = n_stb
        if n_stb_ust_id is not UNSET:
            field_dict["nStbUstID"] = n_stb_ust_id
        if n_stb_none_ust_id is not UNSET:
            field_dict["nStbNoneUstID"] = n_stb_none_ust_id
        if n_stb_im is not UNSET:
            field_dict["nStbIm"] = n_stb_im
        if revc is not UNSET:
            field_dict["revc"] = revc
        if ig is not UNSET:
            field_dict["IG"] = ig
        if al is not UNSET:
            field_dict["AL"] = al
        if s_stfr is not UNSET:
            field_dict["sStfr"] = s_stfr
        if small_business is not UNSET:
            field_dict["smallBusiness"] = small_business

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_null(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        null = _parse_null(d.pop("NULL", UNSET))

        def _parse_n_stb(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        n_stb = _parse_n_stb(d.pop("nStb", UNSET))

        def _parse_n_stb_ust_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        n_stb_ust_id = _parse_n_stb_ust_id(d.pop("nStbUstID", UNSET))

        def _parse_n_stb_none_ust_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        n_stb_none_ust_id = _parse_n_stb_none_ust_id(d.pop("nStbNoneUstID", UNSET))

        def _parse_n_stb_im(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        n_stb_im = _parse_n_stb_im(d.pop("nStbIm", UNSET))

        def _parse_revc(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        revc = _parse_revc(d.pop("revc", UNSET))

        def _parse_ig(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        ig = _parse_ig(d.pop("IG", UNSET))

        def _parse_al(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        al = _parse_al(d.pop("AL", UNSET))

        def _parse_s_stfr(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        s_stfr = _parse_s_stfr(d.pop("sStfr", UNSET))

        def _parse_small_business(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        small_business = _parse_small_business(d.pop("smallBusiness", UNSET))

        position_export_identifier_extended = cls(
            null=null,
            n_stb=n_stb,
            n_stb_ust_id=n_stb_ust_id,
            n_stb_none_ust_id=n_stb_none_ust_id,
            n_stb_im=n_stb_im,
            revc=revc,
            ig=ig,
            al=al,
            s_stfr=s_stfr,
            small_business=small_business,
        )

        position_export_identifier_extended.additional_properties = d
        return position_export_identifier_extended

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
