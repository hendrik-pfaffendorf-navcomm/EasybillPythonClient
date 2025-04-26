from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.documents import Documents
from ...models.get_documents_is_archive import GetDocumentsIsArchive
from ...models.get_documents_is_draft import GetDocumentsIsDraft
from ...models.get_documents_type import GetDocumentsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    type_: Union[Unset, GetDocumentsType] = UNSET,
    is_draft: Union[Unset, GetDocumentsIsDraft] = UNSET,
    is_archive: Union[Unset, GetDocumentsIsArchive] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    ref_id: Union[Unset, str] = UNSET,
    document_date: Union[Unset, str] = UNSET,
    paid_at: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    cancel_id: Union[Unset, str] = UNSET,
    fulfillment_country: Union[Unset, str] = UNSET,
    vat_country: Union[Unset, str] = UNSET,
    shipping_country: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["page"] = page

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_is_draft: Union[Unset, str] = UNSET
    if not isinstance(is_draft, Unset):
        json_is_draft = is_draft.value

    params["is_draft"] = json_is_draft

    json_is_archive: Union[Unset, str] = UNSET
    if not isinstance(is_archive, Unset):
        json_is_archive = is_archive.value

    params["is_archive"] = json_is_archive

    params["customer_id"] = customer_id

    params["project_id"] = project_id

    params["ref_id"] = ref_id

    params["document_date"] = document_date

    params["paid_at"] = paid_at

    params["title"] = title

    params["number"] = number

    params["cancel_id"] = cancel_id

    params["fulfillment_country"] = fulfillment_country

    params["vat_country"] = vat_country

    params["shipping_country"] = shipping_country

    params["status"] = status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Documents]]:
    if response.status_code == 200:
        response_200 = Documents.from_dict(response.json())

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
) -> Response[Union[Any, Documents]]:
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
    type_: Union[Unset, GetDocumentsType] = UNSET,
    is_draft: Union[Unset, GetDocumentsIsDraft] = UNSET,
    is_archive: Union[Unset, GetDocumentsIsArchive] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    ref_id: Union[Unset, str] = UNSET,
    document_date: Union[Unset, str] = UNSET,
    paid_at: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    cancel_id: Union[Unset, str] = UNSET,
    fulfillment_country: Union[Unset, str] = UNSET,
    vat_country: Union[Unset, str] = UNSET,
    shipping_country: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Documents]]:
    """Fetch documents list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        type_ (Union[Unset, GetDocumentsType]):
        is_draft (Union[Unset, GetDocumentsIsDraft]):
        is_archive (Union[Unset, GetDocumentsIsArchive]):
        customer_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        ref_id (Union[Unset, str]):
        document_date (Union[Unset, str]):
        paid_at (Union[Unset, str]):
        title (Union[Unset, str]):
        number (Union[Unset, str]):
        cancel_id (Union[Unset, str]):
        fulfillment_country (Union[Unset, str]):
        vat_country (Union[Unset, str]):
        shipping_country (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Documents]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        type_=type_,
        is_draft=is_draft,
        is_archive=is_archive,
        customer_id=customer_id,
        project_id=project_id,
        ref_id=ref_id,
        document_date=document_date,
        paid_at=paid_at,
        title=title,
        number=number,
        cancel_id=cancel_id,
        fulfillment_country=fulfillment_country,
        vat_country=vat_country,
        shipping_country=shipping_country,
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
    type_: Union[Unset, GetDocumentsType] = UNSET,
    is_draft: Union[Unset, GetDocumentsIsDraft] = UNSET,
    is_archive: Union[Unset, GetDocumentsIsArchive] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    ref_id: Union[Unset, str] = UNSET,
    document_date: Union[Unset, str] = UNSET,
    paid_at: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    cancel_id: Union[Unset, str] = UNSET,
    fulfillment_country: Union[Unset, str] = UNSET,
    vat_country: Union[Unset, str] = UNSET,
    shipping_country: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Documents]]:
    """Fetch documents list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        type_ (Union[Unset, GetDocumentsType]):
        is_draft (Union[Unset, GetDocumentsIsDraft]):
        is_archive (Union[Unset, GetDocumentsIsArchive]):
        customer_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        ref_id (Union[Unset, str]):
        document_date (Union[Unset, str]):
        paid_at (Union[Unset, str]):
        title (Union[Unset, str]):
        number (Union[Unset, str]):
        cancel_id (Union[Unset, str]):
        fulfillment_country (Union[Unset, str]):
        vat_country (Union[Unset, str]):
        shipping_country (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Documents]
    """

    return sync_detailed(
        client=client,
        limit=limit,
        page=page,
        type_=type_,
        is_draft=is_draft,
        is_archive=is_archive,
        customer_id=customer_id,
        project_id=project_id,
        ref_id=ref_id,
        document_date=document_date,
        paid_at=paid_at,
        title=title,
        number=number,
        cancel_id=cancel_id,
        fulfillment_country=fulfillment_country,
        vat_country=vat_country,
        shipping_country=shipping_country,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    type_: Union[Unset, GetDocumentsType] = UNSET,
    is_draft: Union[Unset, GetDocumentsIsDraft] = UNSET,
    is_archive: Union[Unset, GetDocumentsIsArchive] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    ref_id: Union[Unset, str] = UNSET,
    document_date: Union[Unset, str] = UNSET,
    paid_at: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    cancel_id: Union[Unset, str] = UNSET,
    fulfillment_country: Union[Unset, str] = UNSET,
    vat_country: Union[Unset, str] = UNSET,
    shipping_country: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Response[Union[Any, Documents]]:
    """Fetch documents list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        type_ (Union[Unset, GetDocumentsType]):
        is_draft (Union[Unset, GetDocumentsIsDraft]):
        is_archive (Union[Unset, GetDocumentsIsArchive]):
        customer_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        ref_id (Union[Unset, str]):
        document_date (Union[Unset, str]):
        paid_at (Union[Unset, str]):
        title (Union[Unset, str]):
        number (Union[Unset, str]):
        cancel_id (Union[Unset, str]):
        fulfillment_country (Union[Unset, str]):
        vat_country (Union[Unset, str]):
        shipping_country (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Documents]]
    """

    kwargs = _get_kwargs(
        limit=limit,
        page=page,
        type_=type_,
        is_draft=is_draft,
        is_archive=is_archive,
        customer_id=customer_id,
        project_id=project_id,
        ref_id=ref_id,
        document_date=document_date,
        paid_at=paid_at,
        title=title,
        number=number,
        cancel_id=cancel_id,
        fulfillment_country=fulfillment_country,
        vat_country=vat_country,
        shipping_country=shipping_country,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    page: Union[Unset, int] = UNSET,
    type_: Union[Unset, GetDocumentsType] = UNSET,
    is_draft: Union[Unset, GetDocumentsIsDraft] = UNSET,
    is_archive: Union[Unset, GetDocumentsIsArchive] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    project_id: Union[Unset, str] = UNSET,
    ref_id: Union[Unset, str] = UNSET,
    document_date: Union[Unset, str] = UNSET,
    paid_at: Union[Unset, str] = UNSET,
    title: Union[Unset, str] = UNSET,
    number: Union[Unset, str] = UNSET,
    cancel_id: Union[Unset, str] = UNSET,
    fulfillment_country: Union[Unset, str] = UNSET,
    vat_country: Union[Unset, str] = UNSET,
    shipping_country: Union[Unset, str] = UNSET,
    status: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, Documents]]:
    """Fetch documents list

    Args:
        limit (Union[Unset, int]):
        page (Union[Unset, int]):
        type_ (Union[Unset, GetDocumentsType]):
        is_draft (Union[Unset, GetDocumentsIsDraft]):
        is_archive (Union[Unset, GetDocumentsIsArchive]):
        customer_id (Union[Unset, str]):
        project_id (Union[Unset, str]):
        ref_id (Union[Unset, str]):
        document_date (Union[Unset, str]):
        paid_at (Union[Unset, str]):
        title (Union[Unset, str]):
        number (Union[Unset, str]):
        cancel_id (Union[Unset, str]):
        fulfillment_country (Union[Unset, str]):
        vat_country (Union[Unset, str]):
        shipping_country (Union[Unset, str]):
        status (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Documents]
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            page=page,
            type_=type_,
            is_draft=is_draft,
            is_archive=is_archive,
            customer_id=customer_id,
            project_id=project_id,
            ref_id=ref_id,
            document_date=document_date,
            paid_at=paid_at,
            title=title,
            number=number,
            cancel_id=cancel_id,
            fulfillment_country=fulfillment_country,
            vat_country=vat_country,
            shipping_country=shipping_country,
            status=status,
        )
    ).parsed
