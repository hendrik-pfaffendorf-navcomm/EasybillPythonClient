from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.time_trackings import TimeTrackings
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    login_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    date_from_at: Union[Unset, str] = UNSET,
    date_thru_at: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    params["login_id"] = login_id

    params["project_id"] = project_id

    params["date_from_at"] = date_from_at

    params["date_thru_at"] = date_thru_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/time-trackings",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TimeTrackings]]:
    if response.status_code == 200:
        response_200 = TimeTrackings.from_dict(response.json())

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
) -> Response[Union[Any, TimeTrackings]]:
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
    login_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    date_from_at: Union[Unset, str] = UNSET,
    date_thru_at: Union[Unset, str] = UNSET,
) -> Response[Union[Any, TimeTrackings]]:
    """Fetch time trackings list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        login_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        date_from_at (Union[Unset, str]):
        date_thru_at (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TimeTrackings]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        login_id=login_id,
        project_id=project_id,
        date_from_at=date_from_at,
        date_thru_at=date_thru_at,
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
    login_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    date_from_at: Union[Unset, str] = UNSET,
    date_thru_at: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, TimeTrackings]]:
    """Fetch time trackings list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        login_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        date_from_at (Union[Unset, str]):
        date_thru_at (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TimeTrackings]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        page=page,
        login_id=login_id,
        project_id=project_id,
        date_from_at=date_from_at,
        date_thru_at=date_thru_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    login_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    date_from_at: Union[Unset, str] = UNSET,
    date_thru_at: Union[Unset, str] = UNSET,
) -> Response[Union[Any, TimeTrackings]]:
    """Fetch time trackings list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        login_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        date_from_at (Union[Unset, str]):
        date_thru_at (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TimeTrackings]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        login_id=login_id,
        project_id=project_id,
        date_from_at=date_from_at,
        date_thru_at=date_thru_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    login_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    date_from_at: Union[Unset, str] = UNSET,
    date_thru_at: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, TimeTrackings]]:
    """Fetch time trackings list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        login_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        date_from_at (Union[Unset, str]):
        date_thru_at (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TimeTrackings]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            page=page,
            login_id=login_id,
            project_id=project_id,
            date_from_at=date_from_at,
            date_thru_at=date_thru_at,
        )
    ).parsed
