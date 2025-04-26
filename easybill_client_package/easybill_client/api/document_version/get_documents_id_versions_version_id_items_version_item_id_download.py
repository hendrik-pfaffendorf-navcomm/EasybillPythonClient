from http import HTTPStatus
from io import BytesIO
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import File, Response


def _get_kwargs(
    id: int,
    version_id: int,
    version_item_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/documents/{id}/versions/{version_id}/items/{version_item_id}/download",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, File]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    version_id: int,
    version_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, File]]:
    """Download a specific file for a single version of a given document

    Args:
        id (int):
        version_id (int):
        version_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        id=id,
        version_id=version_id,
        version_item_id=version_item_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    version_id: int,
    version_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, File]]:
    """Download a specific file for a single version of a given document

    Args:
        id (int):
        version_id (int):
        version_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return sync_detailed(
        id=id,
        version_id=version_id,
        version_item_id=version_item_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    version_id: int,
    version_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, File]]:
    """Download a specific file for a single version of a given document

    Args:
        id (int):
        version_id (int):
        version_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        id=id,
        version_id=version_id,
        version_item_id=version_item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    version_id: int,
    version_item_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, File]]:
    """Download a specific file for a single version of a given document

    Args:
        id (int):
        version_id (int):
        version_item_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return (
        await asyncio_detailed(
            id=id,
            version_id=version_id,
            version_item_id=version_item_id,
            client=client,
        )
    ).parsed
