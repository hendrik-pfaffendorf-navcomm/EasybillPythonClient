from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.web_hook_content_type import WebHookContentType
from ..models.web_hook_events_item import WebHookEventsItem
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.web_hook_last_response import WebHookLastResponse


T = TypeVar("T", bound="WebHook")


@_attrs_define
class WebHook:
    content_type: WebHookContentType
    description: str
    events: list[WebHookEventsItem]
    secret: str
    url: str
    id: Union[Unset, int] = UNSET
    is_active: Union[Unset, bool] = False
    last_response: Union[Unset, "WebHookLastResponse"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type.value

        description = self.description

        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)

        secret = self.secret

        url = self.url

        id = self.id

        is_active = self.is_active

        last_response: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.last_response, Unset):
            last_response = self.last_response.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content_type": content_type,
                "description": description,
                "events": events,
                "secret": secret,
                "url": url,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if last_response is not UNSET:
            field_dict["last_response"] = last_response

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.web_hook_last_response import WebHookLastResponse

        d = dict(src_dict)
        content_type = WebHookContentType(d.pop("content_type"))

        description = d.pop("description")

        events = []
        _events = d.pop("events")
        for events_item_data in _events:
            events_item = WebHookEventsItem(events_item_data)

            events.append(events_item)

        secret = d.pop("secret")

        url = d.pop("url")

        id = d.pop("id", UNSET)

        is_active = d.pop("is_active", UNSET)

        _last_response = d.pop("last_response", UNSET)
        last_response: Union[Unset, WebHookLastResponse]
        if isinstance(_last_response, Unset):
            last_response = UNSET
        else:
            last_response = WebHookLastResponse.from_dict(_last_response)

        web_hook = cls(
            content_type=content_type,
            description=description,
            events=events,
            secret=secret,
            url=url,
            id=id,
            is_active=is_active,
            last_response=last_response,
        )

        web_hook.additional_properties = d
        return web_hook

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
