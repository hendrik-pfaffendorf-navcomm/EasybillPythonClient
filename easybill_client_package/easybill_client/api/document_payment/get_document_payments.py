from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_payments import DocumentPayments
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    document_id: Union[Unset, str] = UNSET,
    payment_at: Union[Unset, str] = UNSET,
    reference: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    params["document_id"] = document_id

    params["payment_at"] = payment_at

    params["reference"] = reference

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/document-payments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DocumentPayments]]:
    if response.status_code == 200:
        response_200 = DocumentPayments.from_dict(response.json())

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
) -> Response[Union[Any, DocumentPayments]]:
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
    document_id: Union[Unset, str] = UNSET,
    payment_at: Union[Unset, str] = UNSET,
    reference: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DocumentPayments]]:
    """Fetch document payments list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        document_id (Union[Unset, str]):
        payment_at (Union[Unset, str]):
        reference (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DocumentPayments]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        document_id=document_id,
        payment_at=payment_at,
        reference=reference,
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
    document_id: Union[Unset, str] = UNSET,
    payment_at: Union[Unset, str] = UNSET,
    reference: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DocumentPayments]]:
    """Fetch document payments list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        document_id (Union[Unset, str]):
        payment_at (Union[Unset, str]):
        reference (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DocumentPayments]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        page=page,
        document_id=document_id,
        payment_at=payment_at,
        reference=reference,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    document_id: Union[Unset, str] = UNSET,
    payment_at: Union[Unset, str] = UNSET,
    reference: Union[Unset, str] = UNSET,
) -> Response[Union[Any, DocumentPayments]]:
    """Fetch document payments list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        document_id (Union[Unset, str]):
        payment_at (Union[Unset, str]):
        reference (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DocumentPayments]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        document_id=document_id,
        payment_at=payment_at,
        reference=reference,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    document_id: Union[Unset, str] = UNSET,
    payment_at: Union[Unset, str] = UNSET,
    reference: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, DocumentPayments]]:
    """Fetch document payments list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        document_id (Union[Unset, str]):
        payment_at (Union[Unset, str]):
        reference (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DocumentPayments]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            page=page,
            document_id=document_id,
            payment_at=payment_at,
            reference=reference,
        )
    ).parsed
