import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeTracking")


@_attrs_define
class TimeTracking:
    description: str
    cleared_at: Union[None, Unset, datetime.datetime] = UNSET
    created_at: Union[Unset, datetime.datetime] = UNSET
    date_from_at: Union[None, Unset, datetime.datetime] = UNSET
    date_thru_at: Union[None, Unset, datetime.datetime] = UNSET
    hourly_rate: Union[Unset, float] = 0.0
    """ Hourly rate in cents (e.g. "150" = 1.50€) """
    id: Union[Unset, int] = UNSET
    note: Union[None, Unset, str] = UNSET
    number: Union[None, Unset, str] = UNSET
    """ Can be chosen freely """
    position_id: Union[None, Unset, int] = UNSET
    project_id: Union[None, Unset, int] = UNSET
    login_id: Union[None, Unset, int] = UNSET
    """ If omitted or null, the currently active login is used. """
    timer_value: Union[None, Unset, int] = UNSET
    """ Tracked time in minutes """
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        cleared_at: Union[None, Unset, str]
        if isinstance(self.cleared_at, Unset):
            cleared_at = UNSET
        elif isinstance(self.cleared_at, datetime.datetime):
            cleared_at = self.cleared_at.isoformat()
        else:
            cleared_at = self.cleared_at

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        date_from_at: Union[None, Unset, str]
        if isinstance(self.date_from_at, Unset):
            date_from_at = UNSET
        elif isinstance(self.date_from_at, datetime.datetime):
            date_from_at = self.date_from_at.isoformat()
        else:
            date_from_at = self.date_from_at

        date_thru_at: Union[None, Unset, str]
        if isinstance(self.date_thru_at, Unset):
            date_thru_at = UNSET
        elif isinstance(self.date_thru_at, datetime.datetime):
            date_thru_at = self.date_thru_at.isoformat()
        else:
            date_thru_at = self.date_thru_at

        hourly_rate = self.hourly_rate

        id = self.id

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        number: Union[None, Unset, str]
        if isinstance(self.number, Unset):
            number = UNSET
        else:
            number = self.number

        position_id: Union[None, Unset, int]
        if isinstance(self.position_id, Unset):
            position_id = UNSET
        else:
            position_id = self.position_id

        project_id: Union[None, Unset, int]
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        login_id: Union[None, Unset, int]
        if isinstance(self.login_id, Unset):
            login_id = UNSET
        else:
            login_id = self.login_id

        timer_value: Union[None, Unset, int]
        if isinstance(self.timer_value, Unset):
            timer_value = UNSET
        else:
            timer_value = self.timer_value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
            }
        )
        if cleared_at is not UNSET:
            field_dict["cleared_at"] = cleared_at
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if date_from_at is not UNSET:
            field_dict["date_from_at"] = date_from_at
        if date_thru_at is not UNSET:
            field_dict["date_thru_at"] = date_thru_at
        if hourly_rate is not UNSET:
            field_dict["hourly_rate"] = hourly_rate
        if id is not UNSET:
            field_dict["id"] = id
        if note is not UNSET:
            field_dict["note"] = note
        if number is not UNSET:
            field_dict["number"] = number
        if position_id is not UNSET:
            field_dict["position_id"] = position_id
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if timer_value is not UNSET:
            field_dict["timer_value"] = timer_value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description")

        def _parse_cleared_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                cleared_at_type_0 = isoparse(data)

                return cleared_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        cleared_at = _parse_cleared_at(d.pop("cleared_at", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_date_from_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_from_at_type_0 = isoparse(data)

                return date_from_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_from_at = _parse_date_from_at(d.pop("date_from_at", UNSET))

        def _parse_date_thru_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                date_thru_at_type_0 = isoparse(data)

                return date_thru_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        date_thru_at = _parse_date_thru_at(d.pop("date_thru_at", UNSET))

        hourly_rate = d.pop("hourly_rate", UNSET)

        id = d.pop("id", UNSET)

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        def _parse_number(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        number = _parse_number(d.pop("number", UNSET))

        def _parse_position_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position_id = _parse_position_id(d.pop("position_id", UNSET))

        def _parse_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_login_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        login_id = _parse_login_id(d.pop("login_id", UNSET))

        def _parse_timer_value(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        timer_value = _parse_timer_value(d.pop("timer_value", UNSET))

        time_tracking = cls(
            description=description,
            cleared_at=cleared_at,
            created_at=created_at,
            date_from_at=date_from_at,
            date_thru_at=date_thru_at,
            hourly_rate=hourly_rate,
            id=id,
            note=note,
            number=number,
            position_id=position_id,
            project_id=project_id,
            login_id=login_id,
            timer_value=timer_value,
        )

        time_tracking.additional_properties = d
        return time_tracking

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
