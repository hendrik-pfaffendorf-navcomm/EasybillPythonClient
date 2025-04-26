from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document import Document
from ...models.post_documents_id_type_type import PostDocumentsIdTypeType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    type_: PostDocumentsIdTypeType,
    *,
    pdf_template: Union[Unset, str] = "DE",
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pdf_template"] = pdf_template

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/documents/{id}/{type_}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Document]]:
    if response.status_code == 201:
        response_201 = Document.from_dict(response.json())

        return response_201
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
) -> Response[Union[Any, Document]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    type_: PostDocumentsIdTypeType,
    *,
    client: Union[AuthenticatedClient, Client],
    pdf_template: Union[Unset, str] = "DE",
) -> Response[Union[Any, Document]]:
    """Convert an existing document to one of a different type

    Args:
        id (int):
        type_ (PostDocumentsIdTypeType):
        pdf_template (Union[Unset, str]):  Default: 'DE'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Document]]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        pdf_template=pdf_template,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    type_: PostDocumentsIdTypeType,
    *,
    client: Union[AuthenticatedClient, Client],
    pdf_template: Union[Unset, str] = "DE",
) -> Optional[Union[Any, Document]]:
    """Convert an existing document to one of a different type

    Args:
        id (int):
        type_ (PostDocumentsIdTypeType):
        pdf_template (Union[Unset, str]):  Default: 'DE'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Document]
    """

    return sync_detailed(
        id=id,
        type_=type_,
        client=client,
        pdf_template=pdf_template,
    ).parsed


async def asyncio_detailed(
    id: int,
    type_: PostDocumentsIdTypeType,
    *,
    client: Union[AuthenticatedClient, Client],
    pdf_template: Union[Unset, str] = "DE",
) -> Response[Union[Any, Document]]:
    """Convert an existing document to one of a different type

    Args:
        id (int):
        type_ (PostDocumentsIdTypeType):
        pdf_template (Union[Unset, str]):  Default: 'DE'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Document]]
    """

    kwargs = _get_kwargs(
        id=id,
        type_=type_,
        pdf_template=pdf_template,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    type_: PostDocumentsIdTypeType,
    *,
    client: Union[AuthenticatedClient, Client],
    pdf_template: Union[Unset, str] = "DE",
) -> Optional[Union[Any, Document]]:
    """Convert an existing document to one of a different type

    Args:
        id (int):
        type_ (PostDocumentsIdTypeType):
        pdf_template (Union[Unset, str]):  Default: 'DE'.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Document]
    """

    return (
        await asyncio_detailed(
            id=id,
            type_=type_,
            client=client,
            pdf_template=pdf_template,
        )
    ).parsed
