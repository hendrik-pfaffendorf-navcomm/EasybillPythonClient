from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customer import Customer
from ...models.put_customers_id_type import PutCustomersIdType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    body: Customer,
    type_: Union[Unset, PutCustomersIdType] = PutCustomersIdType.CUSTOMER,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/customers/{id}",
        "params": params,
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Customer]]:
    if response.status_code == 200:
        response_200 = Customer.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, Customer]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Customer,
    type_: Union[Unset, PutCustomersIdType] = PutCustomersIdType.CUSTOMER,
) -> Response[Union[Any, Customer]]:
    """Update Customer

    Args:
        id (int):
        type_ (Union[Unset, PutCustomersIdType]):  Default: PutCustomersIdType.CUSTOMER.
        body (Customer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Customer]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Customer,
    type_: Union[Unset, PutCustomersIdType] = PutCustomersIdType.CUSTOMER,
) -> Optional[Union[Any, Customer]]:
    """Update Customer

    Args:
        id (int):
        type_ (Union[Unset, PutCustomersIdType]):  Default: PutCustomersIdType.CUSTOMER.
        body (Customer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Customer]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Customer,
    type_: Union[Unset, PutCustomersIdType] = PutCustomersIdType.CUSTOMER,
) -> Response[Union[Any, Customer]]:
    """Update Customer

    Args:
        id (int):
        type_ (Union[Unset, PutCustomersIdType]):  Default: PutCustomersIdType.CUSTOMER.
        body (Customer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Customer]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Customer,
    type_: Union[Unset, PutCustomersIdType] = PutCustomersIdType.CUSTOMER,
) -> Optional[Union[Any, Customer]]:
    """Update Customer

    Args:
        id (int):
        type_ (Union[Unset, PutCustomersIdType]):  Default: PutCustomersIdType.CUSTOMER.
        body (Customer):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Customer]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
            type_=type_,
        )
    ).parsed
