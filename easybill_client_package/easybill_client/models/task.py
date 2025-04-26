import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.task_category import TaskCategory
from ..models.task_priority import TaskPriority
from ..models.task_status import TaskStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="Task")


@_attrs_define
class Task:
    name: str
    status: TaskStatus
    category: Union[Unset, TaskCategory] = UNSET
    category_custom: Union[None, Unset, str] = UNSET
    """ The name of your custom category. Can only have a value if "category" is "CUSTOM". """
    created_at: Union[Unset, datetime.datetime] = UNSET
    customer_id: Union[None, Unset, int] = UNSET
    description: Union[None, Unset, str] = UNSET
    document_id: Union[None, Unset, int] = UNSET
    end_at: Union[None, Unset, datetime.datetime] = UNSET
    """ The deadline """
    finish_at: Union[None, Unset, datetime.datetime] = UNSET
    """ The time when the task was marked as done """
    id: Union[Unset, int] = UNSET
    login_id: Union[None, Unset, int] = UNSET
    """ When omitted or null, the currently active login is used """
    position_id: Union[None, Unset, int] = UNSET
    priority: Union[Unset, TaskPriority] = TaskPriority.NORMAL
    project_id: Union[None, Unset, int] = UNSET
    start_at: Union[None, Unset, datetime.datetime] = UNSET
    status_percent: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status = self.status.value

        category: Union[Unset, str] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.value

        category_custom: Union[None, Unset, str]
        if isinstance(self.category_custom, Unset):
            category_custom = UNSET
        else:
            category_custom = self.category_custom

        created_at: Union[Unset, str] = UNSET
        if not isinstance(self.created_at, Unset):
            created_at = self.created_at.isoformat()

        customer_id: Union[None, Unset, int]
        if isinstance(self.customer_id, Unset):
            customer_id = UNSET
        else:
            customer_id = self.customer_id

        description: Union[None, Unset, str]
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        document_id: Union[None, Unset, int]
        if isinstance(self.document_id, Unset):
            document_id = UNSET
        else:
            document_id = self.document_id

        end_at: Union[None, Unset, str]
        if isinstance(self.end_at, Unset):
            end_at = UNSET
        elif isinstance(self.end_at, datetime.datetime):
            end_at = self.end_at.isoformat()
        else:
            end_at = self.end_at

        finish_at: Union[None, Unset, str]
        if isinstance(self.finish_at, Unset):
            finish_at = UNSET
        elif isinstance(self.finish_at, datetime.datetime):
            finish_at = self.finish_at.isoformat()
        else:
            finish_at = self.finish_at

        id = self.id

        login_id: Union[None, Unset, int]
        if isinstance(self.login_id, Unset):
            login_id = UNSET
        else:
            login_id = self.login_id

        position_id: Union[None, Unset, int]
        if isinstance(self.position_id, Unset):
            position_id = UNSET
        else:
            position_id = self.position_id

        priority: Union[Unset, str] = UNSET
        if not isinstance(self.priority, Unset):
            priority = self.priority.value

        project_id: Union[None, Unset, int]
        if isinstance(self.project_id, Unset):
            project_id = UNSET
        else:
            project_id = self.project_id

        start_at: Union[None, Unset, str]
        if isinstance(self.start_at, Unset):
            start_at = UNSET
        elif isinstance(self.start_at, datetime.datetime):
            start_at = self.start_at.isoformat()
        else:
            start_at = self.start_at

        status_percent: Union[None, Unset, int]
        if isinstance(self.status_percent, Unset):
            status_percent = UNSET
        else:
            status_percent = self.status_percent

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "status": status,
            }
        )
        if category is not UNSET:
            field_dict["category"] = category
        if category_custom is not UNSET:
            field_dict["category_custom"] = category_custom
        if created_at is not UNSET:
            field_dict["created_at"] = created_at
        if customer_id is not UNSET:
            field_dict["customer_id"] = customer_id
        if description is not UNSET:
            field_dict["description"] = description
        if document_id is not UNSET:
            field_dict["document_id"] = document_id
        if end_at is not UNSET:
            field_dict["end_at"] = end_at
        if finish_at is not UNSET:
            field_dict["finish_at"] = finish_at
        if id is not UNSET:
            field_dict["id"] = id
        if login_id is not UNSET:
            field_dict["login_id"] = login_id
        if position_id is not UNSET:
            field_dict["position_id"] = position_id
        if priority is not UNSET:
            field_dict["priority"] = priority
        if project_id is not UNSET:
            field_dict["project_id"] = project_id
        if start_at is not UNSET:
            field_dict["start_at"] = start_at
        if status_percent is not UNSET:
            field_dict["status_percent"] = status_percent

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        status = TaskStatus(d.pop("status"))

        _category = d.pop("category", UNSET)
        category: Union[Unset, TaskCategory]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = TaskCategory(_category)

        def _parse_category_custom(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        category_custom = _parse_category_custom(d.pop("category_custom", UNSET))

        _created_at = d.pop("created_at", UNSET)
        created_at: Union[Unset, datetime.datetime]
        if isinstance(_created_at, Unset):
            created_at = UNSET
        else:
            created_at = isoparse(_created_at)

        def _parse_customer_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        customer_id = _parse_customer_id(d.pop("customer_id", UNSET))

        def _parse_description(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_document_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        document_id = _parse_document_id(d.pop("document_id", UNSET))

        def _parse_end_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_at_type_0 = isoparse(data)

                return end_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        end_at = _parse_end_at(d.pop("end_at", UNSET))

        def _parse_finish_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                finish_at_type_0 = isoparse(data)

                return finish_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        finish_at = _parse_finish_at(d.pop("finish_at", UNSET))

        id = d.pop("id", UNSET)

        def _parse_login_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        login_id = _parse_login_id(d.pop("login_id", UNSET))

        def _parse_position_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        position_id = _parse_position_id(d.pop("position_id", UNSET))

        _priority = d.pop("priority", UNSET)
        priority: Union[Unset, TaskPriority]
        if isinstance(_priority, Unset):
            priority = UNSET
        else:
            priority = TaskPriority(_priority)

        def _parse_project_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        project_id = _parse_project_id(d.pop("project_id", UNSET))

        def _parse_start_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                start_at_type_0 = isoparse(data)

                return start_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        start_at = _parse_start_at(d.pop("start_at", UNSET))

        def _parse_status_percent(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        status_percent = _parse_status_percent(d.pop("status_percent", UNSET))

        task = cls(
            name=name,
            status=status,
            category=category,
            category_custom=category_custom,
            created_at=created_at,
            customer_id=customer_id,
            description=description,
            document_id=document_id,
            end_at=end_at,
            finish_at=finish_at,
            id=id,
            login_id=login_id,
            position_id=position_id,
            priority=priority,
            project_id=project_id,
            start_at=start_at,
            status_percent=status_percent,
        )

        task.additional_properties = d
        return task

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
