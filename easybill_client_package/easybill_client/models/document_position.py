from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.document_position_cost_price_charge_type import DocumentPositionCostPriceChargeType
from ..models.document_position_discount_type import DocumentPositionDiscountType
from ..models.document_position_item_type import DocumentPositionItemType
from ..models.document_position_type import DocumentPositionType
from ..types import UNSET, Unset

T = TypeVar("T", bound="DocumentPosition")


@_attrs_define
class DocumentPosition:
    number: Union[None, Unset, str] = UNSET
    description: Union[None, Unset, str] = UNSET
    document_note: Union[Unset, str] = UNSET
    """ This field can be used in the document text areas with the liquid placeholder {{document.item_notes}}. Every
    note is only displayed once for every kind of product. This is useful if you want to add something like an
    instruction. """
    quantity: Union[Unset, float] = 1.0
    quantity_str: Union[Unset, str] = UNSET
    """ Use quantity_str if you want to set a quantity like: 1:30 h or 3x5 m. quantity_str overwrites quantity. """
    unit: Union[None, Unset, str] = UNSET
    type_: Union[Unset, DocumentPositionType] = DocumentPositionType.POSITION
    position: Union[Unset, int] = UNSET
    """ Automatic by default (first item: 1, second item: 2, ...) """
    single_price_net: Union[None, Unset, float] = UNSET
    single_price_gross: Union[Unset, float] = UNSET
    vat_percent: Union[Unset, float] = 0.0
    discount: Union[None, Unset, float] = UNSET
    discount_type: Union[Unset, DocumentPositionDiscountType] = UNSET
    position_id: Union[None, Unset, int] = UNSET
    """ If set, values are copied from the referenced position """
    total_price_net: Union[Unset, float] = UNSET
    total_price_gross: Union[Unset, float] = UNSET
    total_vat: Union[Unset, float] = UNSET
    serial_number_id: Union[Unset, str] = UNSET
    serial_number: Union[Unset, str] = UNSET
    booking_account: Union[None, Unset, str] = UNSET
    export_cost_1: Union[None, Unset, str] = UNSET
    export_cost_2: Union[None, Unset, str] = UNSET
    cost_price_net: Union[None, Unset, float] = UNSET
    cost_price_total: Union[Unset, float] = UNSET
    cost_price_charge: Union[Unset, float] = UNSET
    cost_price_charge_type: Union[Unset, DocumentPositionCostPriceChargeType] = UNSET
    item_type: Union[Unset, DocumentPositionItemType] = DocumentPositionItemType.UNDEFINED
    id: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number: Union[None, Unset, str]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        document_note = self.document_note

        quantity = self.quantity

        quantity_str = self.quantity_str

        unit: Union[None, Unset, str]
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        position = self.position

        single_price_net: Union[None, Unset, float]
        if isinstance(self.single_price_net, Unset):
            single_price_net = UNSET
        else:
            single_price_net = self.single_price_net

        single_price_gross = self.single_price_gross

        vat_percent = self.vat_percent

        discount: Union[None, Unset, float]
        if isinstance(self.discount, Unset):
            discount = UNSET
        else:
            discount = self.discount

        discount_type: Union[Unset, str] = UNSET
        if not isinstance(self.discount_type, Unset):
            discount_type = self.discount_type.value

        position_id: Union[None, Unset, int]
        if isinstance(self.position_id, Unset):
            position_id = UNSET
        else:
            position_id = self.position_id

        total_price_net = self.total_price_net

        total_price_gross = self.total_price_gross

        total_vat = self.total_vat

        serial_number_id = self.serial_number_id

        serial_number = self.serial_number

        booking_account: Union[None, Unset, str]
        if isinstance(self.booking_account, Unset):
            booking_account = UNSET
        else:
            booking_account = self.booking_account

        export_cost_1: Union[None, Unset, str]
        if isinstance(self.export_cost_1, Unset):
            export_cost_1 = UNSET
        else:
            export_cost_1 = self.export_cost_1

        export_cost_2: Union[None, Unset, str]
        if isinstance(self.export_cost_2, Unset):
            export_cost_2 = UNSET
        else:
            export_cost_2 = self.export_cost_2

        cost_price_net: Union[None, Unset, float]
        if isinstance(self.cost_price_net, Unset):
            cost_price_net = UNSET
        else:
            cost_price_net = self.cost_price_net

        cost_price_total = self.cost_price_total

        cost_price_charge = self.cost_price_charge

        cost_price_charge_type: Union[Unset, str] = UNSET
        if not isinstance(self.cost_price_charge_type, Unset):
            cost_price_charge_type = self.cost_price_charge_type.value

        item_type: Union[Unset, str] = UNSET
        if not isinstance(self.item_type, Unset):
            item_type = self.item_type.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if number is not UNSET:
            field_dict["number"] = number
        if description is not UNSET:
            field_dict["description"] = description
        if document_note is not UNSET:
            field_dict["document_note"] = document_note
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if quantity_str is not UNSET:
            field_dict["quantity_str"] = quantity_str
        if unit is not UNSET:
            field_dict["unit"] = unit
        if type_ is not UNSET:
            field_dict["type"] = type_
        if position is not UNSET:
            field_dict["position"] = position
        if single_price_net is not UNSET:
            field_dict["single_price_net"] = single_price_net
        if single_price_gross is not UNSET:
            field_dict["single_price_gross"] = single_price_gross
        if vat_percent is not UNSET:
            field_dict["vat_percent"] = vat_percent
        if discount is not UNSET:
            field_dict["discount"] = discount
        if discount_type is not UNSET:
            field_dict["discount_type"] = discount_type
        if position_id is not UNSET:
            field_dict["position_id"] = position_id
        if total_price_net is not UNSET:
            field_dict["total_price_net"] = total_price_net
        if total_price_gross is not UNSET:
            field_dict["total_price_gross"] = total_price_gross
        if total_vat is not UNSET:
            field_dict["total_vat"] = total_vat
        if serial_number_id is not UNSET:
            field_dict["serial_number_id"] = serial_number_id
        if serial_number is not UNSET:
            field_dict["serial_number"] = serial_number
        if booking_account is not UNSET:
            field_dict["booking_account"] = booking_account
        if export_cost_1 is not UNSET:
            field_dict["export_cost_1"] = export_cost_1
        if export_cost_2 is not UNSET:
            field_dict["export_cost_2"] = export_cost_2
        if cost_price_net is not UNSET:
            field_dict["cost_price_net"] = cost_price_net
        if cost_price_total is not UNSET:
            field_dict["cost_price_total"] = cost_price_total
        if cost_price_charge is not UNSET:
            field_dict["cost_price_charge"] = cost_price_charge
        if cost_price_charge_type is not UNSET:
            field_dict["cost_price_charge_type"] = cost_price_charge_type
        if item_type is not UNSET:
            field_dict["itemType"] = item_type
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        document_note = d.pop("document_note", UNSET)

        quantity = d.pop("quantity", UNSET)

        quantity_str = d.pop("quantity_str", UNSET)

        def _parse_unit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unit = _parse_unit(d.pop("unit", UNSET))

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, DocumentPositionType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = DocumentPositionType(_type_)

        position = d.pop("position", UNSET)

        def _parse_single_price_net(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        single_price_net = _parse_single_price_net(d.pop("single_price_net", UNSET))

        single_price_gross = d.pop("single_price_gross", UNSET)

        vat_percent = d.pop("vat_percent", UNSET)

        def _parse_discount(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        discount = _parse_discount(d.pop("discount", UNSET))

        _discount_type = d.pop("discount_type", UNSET)
        discount_type: Union[Unset, DocumentPositionDiscountType]
        if isinstance(_discount_type, Unset):
            discount_type = UNSET
        else:
            discount_type = DocumentPositionDiscountType(_discount_type)

        def _parse_position_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position_id = _parse_position_id(d.pop("position_id", UNSET))

        total_price_net = d.pop("total_price_net", UNSET)

        total_price_gross = d.pop("total_price_gross", UNSET)

        total_vat = d.pop("total_vat", UNSET)

        serial_number_id = d.pop("serial_number_id", UNSET)

        serial_number = d.pop("serial_number", UNSET)

        def _parse_booking_account(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        booking_account = _parse_booking_account(d.pop("booking_account", UNSET))

        def _parse_export_cost_1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        export_cost_1 = _parse_export_cost_1(d.pop("export_cost_1", UNSET))

        def _parse_export_cost_2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        export_cost_2 = _parse_export_cost_2(d.pop("export_cost_2", UNSET))

        def _parse_cost_price_net(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_price_net = _parse_cost_price_net(d.pop("cost_price_net", UNSET))

        cost_price_total = d.pop("cost_price_total", UNSET)

        cost_price_charge = d.pop("cost_price_charge", UNSET)

        _cost_price_charge_type = d.pop("cost_price_charge_type", UNSET)
        cost_price_charge_type: Union[Unset, DocumentPositionCostPriceChargeType]
        if isinstance(_cost_price_charge_type, Unset):
            cost_price_charge_type = UNSET
        else:
            cost_price_charge_type = DocumentPositionCostPriceChargeType(_cost_price_charge_type)

        _item_type = d.pop("itemType", UNSET)
        item_type: Union[Unset, DocumentPositionItemType]
        if isinstance(_item_type, Unset):
            item_type = UNSET
        else:
            item_type = DocumentPositionItemType(_item_type)

        id = d.pop("id", UNSET)

        document_position = cls(
            number=number,
            description=description,
            document_note=document_note,
            quantity=quantity,
            quantity_str=quantity_str,
            unit=unit,
            type_=type_,
            position=position,
            single_price_net=single_price_net,
            single_price_gross=single_price_gross,
            vat_percent=vat_percent,
            discount=discount,
            discount_type=discount_type,
            position_id=position_id,
            total_price_net=total_price_net,
            total_price_gross=total_price_gross,
            total_vat=total_vat,
            serial_number_id=serial_number_id,
            serial_number=serial_number,
            booking_account=booking_account,
            export_cost_1=export_cost_1,
            export_cost_2=export_cost_2,
            cost_price_net=cost_price_net,
            cost_price_total=cost_price_total,
            cost_price_charge=cost_price_charge,
            cost_price_charge_type=cost_price_charge_type,
            item_type=item_type,
            id=id,
        )

        document_position.additional_properties = d
        return document_position

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
