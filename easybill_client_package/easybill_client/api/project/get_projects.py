from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_projects_status import GetProjectsStatus
from ...models.projects import Projects
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    status: Union[Unset, GetProjectsStatus] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    params["customer_id"] = customer_id

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Projects]]:
    if response.status_code == 200:
        response_200 = Projects.from_dict(response.json())

        return response_200
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Projects]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    status: Union[Unset, GetProjectsStatus] = UNSET,
) -> Response[Union[Any, Projects]]:
    """Fetch projects list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        customer_id (Union[Unset, str]):
        status (Union[Unset, GetProjectsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Projects]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        customer_id=customer_id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    status: Union[Unset, GetProjectsStatus] = UNSET,
) -> Optional[Union[Any, Projects]]:
    """Fetch projects list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        customer_id (Union[Unset, str]):
        status (Union[Unset, GetProjectsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Projects]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        page=page,
        customer_id=customer_id,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    status: Union[Unset, GetProjectsStatus] = UNSET,
) -> Response[Union[Any, Projects]]:
    """Fetch projects list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        customer_id (Union[Unset, str]):
        status (Union[Unset, GetProjectsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Projects]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        customer_id=customer_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    status: Union[Unset, GetProjectsStatus] = UNSET,
) -> Optional[Union[Any, Projects]]:
    """Fetch projects list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        customer_id (Union[Unset, str]):
        status (Union[Unset, GetProjectsStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Projects]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            page=page,
            customer_id=customer_id,
            status=status,
        )
    ).parsed
