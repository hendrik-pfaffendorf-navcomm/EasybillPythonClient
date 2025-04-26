from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.login_login_type import LoginLoginType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.login_security import LoginSecurity


T = TypeVar("T", bound="Login")


@_attrs_define
class Login:
    id: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    phone: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    email_signature: Union[Unset, str] = UNSET
    login_type: Union[Unset, LoginLoginType] = LoginLoginType.ASSISTANT
    locale: Union[Unset, str] = UNSET
    time_zone: Union[Unset, str] = UNSET
    security: Union[Unset, "LoginSecurity"] = UNSET
    """ This object is only displayed if your request the login resource as an admin. Otherwise this property will
    be null. """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        display_name = self.display_name

        phone = self.phone

        email = self.email

        email_signature = self.email_signature

        login_type: Union[Unset, str] = UNSET
        if not isinstance(self.login_type, Unset):
            login_type = self.login_type.value

        locale = self.locale

        time_zone = self.time_zone

        security: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.security, Unset):
            security = self.security.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if phone is not UNSET:
            field_dict["phone"] = phone
        if email is not UNSET:
            field_dict["email"] = email
        if email_signature is not UNSET:
            field_dict["email_signature"] = email_signature
        if login_type is not UNSET:
            field_dict["login_type"] = login_type
        if locale is not UNSET:
            field_dict["locale"] = locale
        if time_zone is not UNSET:
            field_dict["time_zone"] = time_zone
        if security is not UNSET:
            field_dict["security"] = security

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.login_security import LoginSecurity

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        display_name = d.pop("display_name", UNSET)

        phone = d.pop("phone", UNSET)

        email = d.pop("email", UNSET)

        email_signature = d.pop("email_signature", UNSET)

        _login_type = d.pop("login_type", UNSET)
        login_type: Union[Unset, LoginLoginType]
        if isinstance(_login_type, Unset):
            login_type = UNSET
        else:
            login_type = LoginLoginType(_login_type)

        locale = d.pop("locale", UNSET)

        time_zone = d.pop("time_zone", UNSET)

        _security = d.pop("security", UNSET)
        security: Union[Unset, LoginSecurity]
        if isinstance(_security, Unset):
            security = UNSET
        else:
            security = LoginSecurity.from_dict(_security)

        login = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            display_name=display_name,
            phone=phone,
            email=email,
            email_signature=email_signature,
            login_type=login_type,
            locale=locale,
            time_zone=time_zone,
            security=security,
        )

        login.additional_properties = d
        return login

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
