from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoginSecurity")


@_attrs_define
class LoginSecurity:
    """This object is only displayed if your request the login resource as an admin. Otherwise this property will be null."""

    two_factor_enabled: Union[Unset, bool] = False
    """ Shows if the login has two factor enabled for the login process """
    recovery_codes_enabled: Union[Unset, bool] = False
    """ Shows if the login has recovery codes enabled to bypass two factor """
    notify_on_new_login_enabled: Union[Unset, bool] = True
    """ Shows if the login has enabled to be notified if a new login is made from an unknown device. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        two_factor_enabled = self.two_factor_enabled

        recovery_codes_enabled = self.recovery_codes_enabled

        notify_on_new_login_enabled = self.notify_on_new_login_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if two_factor_enabled is not UNSET:
            field_dict["two_factor_enabled"] = two_factor_enabled
        if recovery_codes_enabled is not UNSET:
            field_dict["recovery_codes_enabled"] = recovery_codes_enabled
        if notify_on_new_login_enabled is not UNSET:
            field_dict["notify_on_new_login_enabled"] = notify_on_new_login_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        two_factor_enabled = d.pop("two_factor_enabled", UNSET)

        recovery_codes_enabled = d.pop("recovery_codes_enabled", UNSET)

        notify_on_new_login_enabled = d.pop("notify_on_new_login_enabled", UNSET)

        login_security = cls(
            two_factor_enabled=two_factor_enabled,
            recovery_codes_enabled=recovery_codes_enabled,
            notify_on_new_login_enabled=notify_on_new_login_enabled,
        )

        login_security.additional_properties = d
        return login_security

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
