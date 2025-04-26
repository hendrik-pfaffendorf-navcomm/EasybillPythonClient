from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.discount_discount_type import DiscountDiscountType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Discount")


@_attrs_define
class Discount:
    customer_id: int
    id: Union[Unset, int] = UNSET
    discount: Union[Unset, int] = UNSET
    """ The discount value depending on "discount_type" """
    discount_type: Union[Unset, DiscountDiscountType] = DiscountDiscountType.PERCENT
    """ AMOUNT subtracts the value in "discount" from the total<br/> QUANTITY subtracts the value in "discount"
    multiplied by quantity<br/> PERCENT uses the value in "discount" as a percentage<br/> FIX sets the value in
    "discount" as the new price """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        customer_id = self.customer_id

        id = self.id

        discount = self.discount

        discount_type: Union[Unset, str] = UNSET
        if not isinstance(self.discount_type, Unset):
            discount_type = self.discount_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "customer_id": customer_id,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if discount is not UNSET:
            field_dict["discount"] = discount
        if discount_type is not UNSET:
            field_dict["discount_type"] = discount_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        customer_id = d.pop("customer_id")

        id = d.pop("id", UNSET)

        discount = d.pop("discount", UNSET)

        _discount_type = d.pop("discount_type", UNSET)
        discount_type: Union[Unset, DiscountDiscountType]
        if isinstance(_discount_type, Unset):
            discount_type = UNSET
        else:
            discount_type = DiscountDiscountType(_discount_type)

        discount = cls(
            customer_id=customer_id,
            id=id,
            discount=discount,
            discount_type=discount_type,
        )

        discount.additional_properties = d
        return discount

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
