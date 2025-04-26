from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_post_boxes_status import GetPostBoxesStatus
from ...models.get_post_boxes_type import GetPostBoxesType
from ...models.post_boxes import PostBoxes
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    type_: Union[Unset, GetPostBoxesType] = UNSET,
    status: Union[Unset, GetPostBoxesStatus] = UNSET,
    document_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["document_id"] = document_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/post-boxes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PostBoxes]]:
    if response.status_code == 200:
        response_200 = PostBoxes.from_dict(response.json())

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
) -> Response[Union[Any, PostBoxes]]:
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
    type_: Union[Unset, GetPostBoxesType] = UNSET,
    status: Union[Unset, GetPostBoxesStatus] = UNSET,
    document_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PostBoxes]]:
    """Fetch post box list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        type_ (Union[Unset, GetPostBoxesType]):
        status (Union[Unset, GetPostBoxesStatus]):
        document_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostBoxes]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        type_=type_,
        status=status,
        document_id=document_id,
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
    type_: Union[Unset, GetPostBoxesType] = UNSET,
    status: Union[Unset, GetPostBoxesStatus] = UNSET,
    document_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PostBoxes]]:
    """Fetch post box list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        type_ (Union[Unset, GetPostBoxesType]):
        status (Union[Unset, GetPostBoxesStatus]):
        document_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostBoxes]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        page=page,
        type_=type_,
        status=status,
        document_id=document_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    type_: Union[Unset, GetPostBoxesType] = UNSET,
    status: Union[Unset, GetPostBoxesStatus] = UNSET,
    document_id: Union[Unset, str] = UNSET,
) -> Response[Union[Any, PostBoxes]]:
    """Fetch post box list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        type_ (Union[Unset, GetPostBoxesType]):
        status (Union[Unset, GetPostBoxesStatus]):
        document_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PostBoxes]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        type_=type_,
        status=status,
        document_id=document_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    type_: Union[Unset, GetPostBoxesType] = UNSET,
    status: Union[Unset, GetPostBoxesStatus] = UNSET,
    document_id: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, PostBoxes]]:
    """Fetch post box list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        type_ (Union[Unset, GetPostBoxesType]):
        status (Union[Unset, GetPostBoxesStatus]):
        document_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PostBoxes]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            page=page,
            type_=type_,
            status=status,
            document_id=document_id,
        )
    ).parsed
