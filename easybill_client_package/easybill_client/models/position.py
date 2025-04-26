from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.position_price_type import PositionPriceType
from ..models.position_stock import PositionStock
from ..models.position_stock_limit_notify_frequency import PositionStockLimitNotifyFrequency
from ..models.position_type import PositionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.position_export_identifier_extended import PositionExportIdentifierExtended


T = TypeVar("T", bound="Position")


@_attrs_define
class Position:
    number: str
    description: str
    """ The positions name or description """
    sale_price: float
    """ Price in cents (e.g. "150" = 1.50€) """
    id: Union[Unset, int] = UNSET
    type_: Union[Unset, PositionType] = PositionType.PRODUCT
    document_note: Union[Unset, str] = UNSET
    """ This field can be used in the document text areas with the liquid placeholder {{document.item_notes}}. Every
    note is only displayed once for every kind of product. This is useful if you want to add something like an
    instruction. """
    note: Union[None, Unset, str] = UNSET
    """ Note for internal use """
    unit: Union[None, Unset, str] = UNSET
    export_identifier: Union[None, Unset, str] = UNSET
    """ The FAS-Account is the four-digit revenue account, in which the revenue will be entered when doing the
    export to your tax consultant. In case you want to split your revenue to several revenue accounts, please talk
    to your tax consultant before, to guarantee an unobstructed use of the interface. For every revenue element,
    there are number ranges, which can be used. Please avoid using combinations of numbers, which can not be used by
    your tax consultant. """
    export_identifier_extended: Union[Unset, "PositionExportIdentifierExtended"] = UNSET
    login_id: Union[Unset, int] = UNSET
    price_type: Union[Unset, PositionPriceType] = PositionPriceType.NETTO
    vat_percent: Union[Unset, float] = 19.0
    sale_price2: Union[None, Unset, float] = UNSET
    """ Price for customers of group 2 in cents (e.g. "150" = 1.50€) """
    sale_price3: Union[None, Unset, float] = UNSET
    """ Price for customers of group 3 in cents (e.g. "150" = 1.50€) """
    sale_price4: Union[None, Unset, float] = UNSET
    """ Price for customers of group 4 in cents (e.g. "150" = 1.50€) """
    sale_price5: Union[None, Unset, float] = UNSET
    """ Price for customers of group 5 in cents (e.g. "150" = 1.50€) """
    sale_price6: Union[None, Unset, float] = UNSET
    """ Price for customers of group 6 in cents (e.g. "150" = 1.50€) """
    sale_price7: Union[None, Unset, float] = UNSET
    """ Price for customers of group 7 in cents (e.g. "150" = 1.50€) """
    sale_price8: Union[None, Unset, float] = UNSET
    """ Price for customers of group 8 in cents (e.g. "150" = 1.50€) """
    sale_price9: Union[None, Unset, float] = UNSET
    """ Price for customers of group 9 in cents (e.g. "150" = 1.50€) """
    sale_price10: Union[None, Unset, float] = UNSET
    """ Price for customers of group 10 in cents (e.g. "150" = 1.50€) """
    cost_price: Union[None, Unset, float] = UNSET
    """ Price in cents (e.g. "150" = 1.50€) """
    export_cost1: Union[None, Unset, str] = UNSET
    export_cost2: Union[None, Unset, str] = UNSET
    group_id: Union[None, Unset, int] = UNSET
    stock: Union[Unset, PositionStock] = PositionStock.NO
    """ Activates stock management for this position """
    stock_count: Union[Unset, int] = UNSET
    """ Current stock count """
    stock_limit_notify: Union[Unset, bool] = False
    """ Notify when stock_count is lower than stock_limit """
    stock_limit_notify_frequency: Union[Unset, PositionStockLimitNotifyFrequency] = (
        PositionStockLimitNotifyFrequency.ALWAYS
    )
    """ Notify frequency when stock_count is lower than stock_limit (ALWAYS, ONCE) """
    stock_limit: Union[Unset, int] = UNSET
    quantity: Union[None, Unset, float] = UNSET
    """ Used as the default quantity when adding this position to a document """
    archived: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        number = self.number

        description = self.description

        sale_price = self.sale_price

        id = self.id

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        document_note = self.document_note

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        unit: Union[None, Unset, str]
        if isinstance(self.unit, Unset):
            unit = UNSET
        else:
            unit = self.unit

        export_identifier: Union[None, Unset, str]
        if isinstance(self.export_identifier, Unset):
            export_identifier = UNSET
        else:
            export_identifier = self.export_identifier

        export_identifier_extended: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.export_identifier_extended, Unset):
            export_identifier_extended = self.export_identifier_extended.to_dict()

        login_id = self.login_id

        price_type: Union[Unset, str] = UNSET
        if not isinstance(self.price_type, Unset):
            price_type = self.price_type.value

        vat_percent = self.vat_percent

        sale_price2: Union[None, Unset, float]
        if isinstance(self.sale_price2, Unset):
            sale_price2 = UNSET
        else:
            sale_price2 = self.sale_price2

        sale_price3: Union[None, Unset, float]
        if isinstance(self.sale_price3, Unset):
            sale_price3 = UNSET
        else:
            sale_price3 = self.sale_price3

        sale_price4: Union[None, Unset, float]
        if isinstance(self.sale_price4, Unset):
            sale_price4 = UNSET
        else:
            sale_price4 = self.sale_price4

        sale_price5: Union[None, Unset, float]
        if isinstance(self.sale_price5, Unset):
            sale_price5 = UNSET
        else:
            sale_price5 = self.sale_price5

        sale_price6: Union[None, Unset, float]
        if isinstance(self.sale_price6, Unset):
            sale_price6 = UNSET
        else:
            sale_price6 = self.sale_price6

        sale_price7: Union[None, Unset, float]
        if isinstance(self.sale_price7, Unset):
            sale_price7 = UNSET
        else:
            sale_price7 = self.sale_price7

        sale_price8: Union[None, Unset, float]
        if isinstance(self.sale_price8, Unset):
            sale_price8 = UNSET
        else:
            sale_price8 = self.sale_price8

        sale_price9: Union[None, Unset, float]
        if isinstance(self.sale_price9, Unset):
            sale_price9 = UNSET
        else:
            sale_price9 = self.sale_price9

        sale_price10: Union[None, Unset, float]
        if isinstance(self.sale_price10, Unset):
            sale_price10 = UNSET
        else:
            sale_price10 = self.sale_price10

        cost_price: Union[None, Unset, float]
        if isinstance(self.cost_price, Unset):
            cost_price = UNSET
        else:
            cost_price = self.cost_price

        export_cost1: Union[None, Unset, str]
        if isinstance(self.export_cost1, Unset):
            export_cost1 = UNSET
        else:
            export_cost1 = self.export_cost1

        export_cost2: Union[None, Unset, str]
        if isinstance(self.export_cost2, Unset):
            export_cost2 = UNSET
        else:
            export_cost2 = self.export_cost2

        group_id: Union[None, Unset, int]
        if isinstance(self.group_id, Unset):
            group_id = UNSET
        else:
            group_id = self.group_id

        stock: Union[Unset, str] = UNSET
        if not isinstance(self.stock, Unset):
            stock = self.stock.value

        stock_count = self.stock_count

        stock_limit_notify = self.stock_limit_notify

        stock_limit_notify_frequency: Union[Unset, str] = UNSET
        if not isinstance(self.stock_limit_notify_frequency, Unset):
            stock_limit_notify_frequency = self.stock_limit_notify_frequency.value

        stock_limit = self.stock_limit

        quantity: Union[None, Unset, float]
        if isinstance(self.quantity, Unset):
            quantity = UNSET
        else:
            quantity = self.quantity

        archived = self.archived

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "number": number,
                "description": description,
                "sale_price": sale_price,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if document_note is not UNSET:
            field_dict["document_note"] = document_note
        if note is not UNSET:
            field_dict["note"] = note
        if unit is not UNSET:
            field_dict["unit"] = unit
        if export_identifier is not UNSET:
            field_dict["export_identifier"] = export_identifier
        if export_identifier_extended is not UNSET:
            field_dict["export_identifier_extended"] = export_identifier_extended
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if price_type is not UNSET:
            field_dict["price_type"] = price_type
        if vat_percent is not UNSET:
            field_dict["vat_percent"] = vat_percent
        if sale_price2 is not UNSET:
            field_dict["sale_price2"] = sale_price2
        if sale_price3 is not UNSET:
            field_dict["sale_price3"] = sale_price3
        if sale_price4 is not UNSET:
            field_dict["sale_price4"] = sale_price4
        if sale_price5 is not UNSET:
            field_dict["sale_price5"] = sale_price5
        if sale_price6 is not UNSET:
            field_dict["sale_price6"] = sale_price6
        if sale_price7 is not UNSET:
            field_dict["sale_price7"] = sale_price7
        if sale_price8 is not UNSET:
            field_dict["sale_price8"] = sale_price8
        if sale_price9 is not UNSET:
            field_dict["sale_price9"] = sale_price9
        if sale_price10 is not UNSET:
            field_dict["sale_price10"] = sale_price10
        if cost_price is not UNSET:
            field_dict["cost_price"] = cost_price
        if export_cost1 is not UNSET:
            field_dict["export_cost1"] = export_cost1
        if export_cost2 is not UNSET:
            field_dict["export_cost2"] = export_cost2
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if stock is not UNSET:
            field_dict["stock"] = stock
        if stock_count is not UNSET:
            field_dict["stock_count"] = stock_count
        if stock_limit_notify is not UNSET:
            field_dict["stock_limit_notify"] = stock_limit_notify
        if stock_limit_notify_frequency is not UNSET:
            field_dict["stock_limit_notify_frequency"] = stock_limit_notify_frequency
        if stock_limit is not UNSET:
            field_dict["stock_limit"] = stock_limit
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if archived is not UNSET:
            field_dict["archived"] = archived

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.position_export_identifier_extended import PositionExportIdentifierExtended

        d = dict(src_dict)
        number = d.pop("number")

        description = d.pop("description")

        sale_price = d.pop("sale_price")

        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, PositionType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PositionType(_type_)

        document_note = d.pop("document_note", UNSET)

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_unit(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        unit = _parse_unit(d.pop("unit", UNSET))

        def _parse_export_identifier(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        export_identifier = _parse_export_identifier(d.pop("export_identifier", UNSET))

        _export_identifier_extended = d.pop("export_identifier_extended", UNSET)
        export_identifier_extended: Union[Unset, PositionExportIdentifierExtended]
        if isinstance(_export_identifier_extended, Unset):
            export_identifier_extended = UNSET
        else:
            export_identifier_extended = PositionExportIdentifierExtended.from_dict(_export_identifier_extended)

        login_id = d.pop("login_id", UNSET)

        _price_type = d.pop("price_type", UNSET)
        price_type: Union[Unset, PositionPriceType]
        if isinstance(_price_type, Unset):
            price_type = UNSET
        else:
            price_type = PositionPriceType(_price_type)

        vat_percent = d.pop("vat_percent", UNSET)

        def _parse_sale_price2(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sale_price2 = _parse_sale_price2(d.pop("sale_price2", UNSET))

        def _parse_sale_price3(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sale_price3 = _parse_sale_price3(d.pop("sale_price3", UNSET))

        def _parse_sale_price4(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sale_price4 = _parse_sale_price4(d.pop("sale_price4", UNSET))

        def _parse_sale_price5(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sale_price5 = _parse_sale_price5(d.pop("sale_price5", UNSET))

        def _parse_sale_price6(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sale_price6 = _parse_sale_price6(d.pop("sale_price6", UNSET))

        def _parse_sale_price7(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sale_price7 = _parse_sale_price7(d.pop("sale_price7", UNSET))

        def _parse_sale_price8(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sale_price8 = _parse_sale_price8(d.pop("sale_price8", UNSET))

        def _parse_sale_price9(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sale_price9 = _parse_sale_price9(d.pop("sale_price9", UNSET))

        def _parse_sale_price10(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        sale_price10 = _parse_sale_price10(d.pop("sale_price10", UNSET))

        def _parse_cost_price(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cost_price = _parse_cost_price(d.pop("cost_price", UNSET))

        def _parse_export_cost1(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        export_cost1 = _parse_export_cost1(d.pop("export_cost1", UNSET))

        def _parse_export_cost2(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        export_cost2 = _parse_export_cost2(d.pop("export_cost2", UNSET))

        def _parse_group_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        group_id = _parse_group_id(d.pop("group_id", UNSET))

        _stock = d.pop("stock", UNSET)
        stock: Union[Unset, PositionStock]
        if isinstance(_stock, Unset):
            stock = UNSET
        else:
            stock = PositionStock(_stock)

        stock_count = d.pop("stock_count", UNSET)

        stock_limit_notify = d.pop("stock_limit_notify", UNSET)

        _stock_limit_notify_frequency = d.pop("stock_limit_notify_frequency", UNSET)
        stock_limit_notify_frequency: Union[Unset, PositionStockLimitNotifyFrequency]
        if isinstance(_stock_limit_notify_frequency, Unset):
            stock_limit_notify_frequency = UNSET
        else:
            stock_limit_notify_frequency = PositionStockLimitNotifyFrequency(_stock_limit_notify_frequency)

        stock_limit = d.pop("stock_limit", UNSET)

        def _parse_quantity(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        quantity = _parse_quantity(d.pop("quantity", UNSET))

        archived = d.pop("archived", UNSET)

        position = cls(
            number=number,
            description=description,
            sale_price=sale_price,
            id=id,
            type_=type_,
            document_note=document_note,
            note=note,
            unit=unit,
            export_identifier=export_identifier,
            export_identifier_extended=export_identifier_extended,
            login_id=login_id,
            price_type=price_type,
            vat_percent=vat_percent,
            sale_price2=sale_price2,
            sale_price3=sale_price3,
            sale_price4=sale_price4,
            sale_price5=sale_price5,
            sale_price6=sale_price6,
            sale_price7=sale_price7,
            sale_price8=sale_price8,
            sale_price9=sale_price9,
            sale_price10=sale_price10,
            cost_price=cost_price,
            export_cost1=export_cost1,
            export_cost2=export_cost2,
            group_id=group_id,
            stock=stock,
            stock_count=stock_count,
            stock_limit_notify=stock_limit_notify,
            stock_limit_notify_frequency=stock_limit_notify_frequency,
            stock_limit=stock_limit,
            quantity=quantity,
            archived=archived,
        )

        position.additional_properties = d
        return position

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
