from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_pdf_templates_type_item import GetPdfTemplatesTypeItem
from ...models.pdf_templates import PDFTemplates
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    type_: Union[Unset, list[GetPdfTemplatesTypeItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: Union[Unset, list[str]] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = []
        for type_item_data in type_:
            type_item = type_item_data.value
            json_type_.append(type_item)

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/pdf-templates",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PDFTemplates]]:
    if response.status_code == 200:
        response_200 = PDFTemplates.from_dict(response.json())

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
) -> Response[Union[Any, PDFTemplates]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, list[GetPdfTemplatesTypeItem]] = UNSET,
) -> Response[Union[Any, PDFTemplates]]:
    """Fetch PDF Templates list

    Args:
        type_ (Union[Unset, list[GetPdfTemplatesTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PDFTemplates]]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, list[GetPdfTemplatesTypeItem]] = UNSET,
) -> Optional[Union[Any, PDFTemplates]]:
    """Fetch PDF Templates list

    Args:
        type_ (Union[Unset, list[GetPdfTemplatesTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PDFTemplates]
    """

    return sync_detailed(
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, list[GetPdfTemplatesTypeItem]] = UNSET,
) -> Response[Union[Any, PDFTemplates]]:
    """Fetch PDF Templates list

    Args:
        type_ (Union[Unset, list[GetPdfTemplatesTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PDFTemplates]]
    """

    kwargs = _get_kwargs(
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, list[GetPdfTemplatesTypeItem]] = UNSET,
) -> Optional[Union[Any, PDFTemplates]]:
    """Fetch PDF Templates list

    Args:
        type_ (Union[Unset, list[GetPdfTemplatesTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PDFTemplates]
    """

    return (
        await asyncio_detailed(
            client=client,
            type_=type_,
        )
    ).parsed
