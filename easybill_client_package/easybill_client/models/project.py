import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.project_budget_notify_frequency import ProjectBudgetNotifyFrequency
from ..models.project_status import ProjectStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    name: str
    budget_amount: Union[Unset, int] = UNSET
    """ Project budget in cents (e.g. "150" = 1.50€) """
    budget_time: Union[Unset, int] = UNSET
    """ Time budget in minutes (e.g. "90" = 1 hour and 30 minutes) """
    customer_id: Union[None, Unset, int] = UNSET
    hourly_rate: Union[Unset, float] = UNSET
    """ Hourly rate in cents (e.g. "150" = 1.50€) """
    id: Union[Unset, int] = UNSET
    login_id: Union[None, Unset, int] = UNSET
    """ If omitted or null, the currently active login is used """
    note: Union[None, Unset, str] = UNSET
    status: Union[Unset, ProjectStatus] = ProjectStatus.OPEN
    due_at: Union[None, Unset, datetime.date] = UNSET
    budget_notify_frequency: Union[Unset, ProjectBudgetNotifyFrequency] = ProjectBudgetNotifyFrequency.ALWAYS
    consumed_time: Union[Unset, int] = UNSET
    consumed_amount: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        budget_amount = self.budget_amount

        budget_time = self.budget_time

        customer_id: Union[None, Unset, int]
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        hourly_rate = self.hourly_rate

        id = self.id

        login_id: Union[None, Unset, int]
        if isinstance(self.login_id, Unset):
            login_id = UNSET
        else:
            login_id = self.login_id

        note: Union[None, Unset, str]
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        due_at: Union[None, Unset, str]
        if isinstance(self.due_at, Unset):
            due_at = UNSET
        elif isinstance(self.due_at, datetime.date):
            due_at = self.due_at.isoformat()
        else:
            due_at = self.due_at

        budget_notify_frequency: Union[Unset, str] = UNSET
        if not isinstance(self.budget_notify_frequency, Unset):
            budget_notify_frequency = self.budget_notify_frequency.value

        consumed_time = self.consumed_time

        consumed_amount = self.consumed_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if budget_amount is not UNSET:
            field_dict["budget_amount"] = budget_amount
        if budget_time is not UNSET:
            field_dict["budget_time"] = budget_time
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if hourly_rate is not UNSET:
            field_dict["hourly_rate"] = hourly_rate
        if id is not UNSET:
            field_dict["id"] = id
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if note is not UNSET:
            field_dict["note"] = note
        if status is not UNSET:
            field_dict["status"] = status
        if due_at is not UNSET:
            field_dict["due_at"] = due_at
        if budget_notify_frequency is not UNSET:
            field_dict["budget_notify_frequency"] = budget_notify_frequency
        if consumed_time is not UNSET:
            field_dict["consumed_time"] = consumed_time
        if consumed_amount is not UNSET:
            field_dict["consumed_amount"] = consumed_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        budget_amount = d.pop("budget_amount", UNSET)

        budget_time = d.pop("budget_time", UNSET)

        def _parse_customer_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        hourly_rate = d.pop("hourly_rate", UNSET)

        id = d.pop("id", UNSET)

        def _parse_login_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        login_id = _parse_login_id(d.pop("login_id", UNSET))

        def _parse_note(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        note = _parse_note(d.pop("note", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, ProjectStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ProjectStatus(_status)

        def _parse_due_at(data: object) -> Union[None, Unset, datetime.date]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                due_at_type_0 = isoparse(data).date()

                return due_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.date], data)

        due_at = _parse_due_at(d.pop("due_at", UNSET))

        _budget_notify_frequency = d.pop("budget_notify_frequency", UNSET)
        budget_notify_frequency: Union[Unset, ProjectBudgetNotifyFrequency]
        if isinstance(_budget_notify_frequency, Unset):
            budget_notify_frequency = UNSET
        else:
            budget_notify_frequency = ProjectBudgetNotifyFrequency(_budget_notify_frequency)

        consumed_time = d.pop("consumed_time", UNSET)

        consumed_amount = d.pop("consumed_amount", UNSET)

        project = cls(
            name=name,
            budget_amount=budget_amount,
            budget_time=budget_time,
            customer_id=customer_id,
            hourly_rate=hourly_rate,
            id=id,
            login_id=login_id,
            note=note,
            status=status,
            due_at=due_at,
            budget_notify_frequency=budget_notify_frequency,
            consumed_time=consumed_time,
            consumed_amount=consumed_amount,
        )

        project.additional_properties = d
        return project

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
