from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.customers import Customers
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    additional_group_id: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    zip_code: Union[Unset, str] = UNSET,
    emails: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    company_name: Union[Unset, str] = UNSET,
    created_at: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    params["group_id"] = group_id

    params["additional_group_id"] = additional_group_id

    params["number"] = number

    params["country"] = country

    params["zip_code"] = zip_code

    params["emails"] = emails

    params["first_name"] = first_name

    params["last_name"] = last_name

    params["company_name"] = company_name

    params["created_at"] = created_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Customers]]:
    if response.status_code == 200:
        response_200 = Customers.from_dict(response.json())

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
) -> Response[Union[Any, Customers]]:
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
    group_id: Union[Unset, str] = UNSET,
    additional_group_id: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    zip_code: Union[Unset, str] = UNSET,
    emails: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    company_name: Union[Unset, str] = UNSET,
    created_at: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Customers]]:
    """Fetch customers list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        group_id (Union[Unset, str]):
        additional_group_id (Union[Unset, str]):
        number (Union[Unset, str]):
        country (Union[Unset, str]):
        zip_code (Union[Unset, str]):
        emails (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        company_name (Union[Unset, str]):
        created_at (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Customers]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        group_id=group_id,
        additional_group_id=additional_group_id,
        number=number,
        country=country,
        zip_code=zip_code,
        emails=emails,
        first_name=first_name,
        last_name=last_name,
        company_name=company_name,
        created_at=created_at,
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
    group_id: Union[Unset, str] = UNSET,
    additional_group_id: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    zip_code: Union[Unset, str] = UNSET,
    emails: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    company_name: Union[Unset, str] = UNSET,
    created_at: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Customers]]:
    """Fetch customers list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        group_id (Union[Unset, str]):
        additional_group_id (Union[Unset, str]):
        number (Union[Unset, str]):
        country (Union[Unset, str]):
        zip_code (Union[Unset, str]):
        emails (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        company_name (Union[Unset, str]):
        created_at (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Customers]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        page=page,
        group_id=group_id,
        additional_group_id=additional_group_id,
        number=number,
        country=country,
        zip_code=zip_code,
        emails=emails,
        first_name=first_name,
        last_name=last_name,
        company_name=company_name,
        created_at=created_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    additional_group_id: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    zip_code: Union[Unset, str] = UNSET,
    emails: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    company_name: Union[Unset, str] = UNSET,
    created_at: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Customers]]:
    """Fetch customers list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        group_id (Union[Unset, str]):
        additional_group_id (Union[Unset, str]):
        number (Union[Unset, str]):
        country (Union[Unset, str]):
        zip_code (Union[Unset, str]):
        emails (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        company_name (Union[Unset, str]):
        created_at (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Customers]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        group_id=group_id,
        additional_group_id=additional_group_id,
        number=number,
        country=country,
        zip_code=zip_code,
        emails=emails,
        first_name=first_name,
        last_name=last_name,
        company_name=company_name,
        created_at=created_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    group_id: Union[Unset, str] = UNSET,
    additional_group_id: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    country: Union[Unset, str] = UNSET,
    zip_code: Union[Unset, str] = UNSET,
    emails: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    company_name: Union[Unset, str] = UNSET,
    created_at: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Customers]]:
    """Fetch customers list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        group_id (Union[Unset, str]):
        additional_group_id (Union[Unset, str]):
        number (Union[Unset, str]):
        country (Union[Unset, str]):
        zip_code (Union[Unset, str]):
        emails (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        company_name (Union[Unset, str]):
        created_at (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Customers]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            page=page,
            group_id=group_id,
            additional_group_id=additional_group_id,
            number=number,
            country=country,
            zip_code=zip_code,
            emails=emails,
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
            created_at=created_at,
        )
    ).parsed
