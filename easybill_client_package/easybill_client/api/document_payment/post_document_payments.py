from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document_payment import DocumentPayment
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: DocumentPayment,
    paid: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["paid"] = paid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/document-payments",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DocumentPayment]]:
    if response.status_code == 201:
        response_201 = DocumentPayment.from_dict(response.json())

        return response_201
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DocumentPayment]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DocumentPayment,
    paid: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, DocumentPayment]]:
    """Create document payment

    Args:
        paid (Union[Unset, bool]):
        body (DocumentPayment):  Example: {'id': 1, 'document_id': 1, 'login_id': 1, 'amount':
            1000, 'payment_at': datetime.datetime(2007, 9, 17, 0, 0,
            tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'type': 'VISA', 'provider':
            'Stripe', 'reference': '111111-VISA-222222-6666'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DocumentPayment]]
    """

    kwargs = _get_kwargs(
        body=body,
        paid=paid,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DocumentPayment,
    paid: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, DocumentPayment]]:
    """Create document payment

    Args:
        paid (Union[Unset, bool]):
        body (DocumentPayment):  Example: {'id': 1, 'document_id': 1, 'login_id': 1, 'amount':
            1000, 'payment_at': datetime.datetime(2007, 9, 17, 0, 0,
            tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'type': 'VISA', 'provider':
            'Stripe', 'reference': '111111-VISA-222222-6666'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DocumentPayment]
    """

    return sync_detailed(
        client=client,
        body=body,
        paid=paid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DocumentPayment,
    paid: Union[Unset, bool] = UNSET,
) -> Response[Union[Any, DocumentPayment]]:
    """Create document payment

    Args:
        paid (Union[Unset, bool]):
        body (DocumentPayment):  Example: {'id': 1, 'document_id': 1, 'login_id': 1, 'amount':
            1000, 'payment_at': datetime.datetime(2007, 9, 17, 0, 0,
            tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'type': 'VISA', 'provider':
            'Stripe', 'reference': '111111-VISA-222222-6666'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DocumentPayment]]
    """

    kwargs = _get_kwargs(
        body=body,
        paid=paid,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DocumentPayment,
    paid: Union[Unset, bool] = UNSET,
) -> Optional[Union[Any, DocumentPayment]]:
    """Create document payment

    Args:
        paid (Union[Unset, bool]):
        body (DocumentPayment):  Example: {'id': 1, 'document_id': 1, 'login_id': 1, 'amount':
            1000, 'payment_at': datetime.datetime(2007, 9, 17, 0, 0,
            tzinfo=datetime.timezone(datetime.timedelta(0), 'Z')), 'type': 'VISA', 'provider':
            'Stripe', 'reference': '111111-VISA-222222-6666'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DocumentPayment]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            paid=paid,
        )
    ).parsed
