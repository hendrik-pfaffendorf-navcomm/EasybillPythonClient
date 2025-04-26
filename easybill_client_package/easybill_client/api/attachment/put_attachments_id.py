from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachment import Attachment
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    body: Attachment,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/attachments/{id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, Attachment]]:
    if response.status_code == 200:
        response_200 = Attachment.from_dict(response.json())

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
) -> Response[Union[Any, Attachment]]:
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
    body: Attachment,
) -> Response[Union[Any, Attachment]]:
    """Update attachment

    Args:
        id (int):
        body (Attachment): If customer_id, project_id and document_id are null, the attachment has
            a global context and is accessible from the web ui. Keep in mind only to provide one of
            the four context. You can't attach a file to several context in one request. A error is
            thrown if you provide two or more context (i. E. sending customer_id, document_id and
            project_id in combination).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Attachment]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attachment,
) -> Optional[Union[Any, Attachment]]:
    """Update attachment

    Args:
        id (int):
        body (Attachment): If customer_id, project_id and document_id are null, the attachment has
            a global context and is accessible from the web ui. Keep in mind only to provide one of
            the four context. You can't attach a file to several context in one request. A error is
            thrown if you provide two or more context (i. E. sending customer_id, document_id and
            project_id in combination).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Attachment]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attachment,
) -> Response[Union[Any, Attachment]]:
    """Update attachment

    Args:
        id (int):
        body (Attachment): If customer_id, project_id and document_id are null, the attachment has
            a global context and is accessible from the web ui. Keep in mind only to provide one of
            the four context. You can't attach a file to several context in one request. A error is
            thrown if you provide two or more context (i. E. sending customer_id, document_id and
            project_id in combination).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, Attachment]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Attachment,
) -> Optional[Union[Any, Attachment]]:
    """Update attachment

    Args:
        id (int):
        body (Attachment): If customer_id, project_id and document_id are null, the attachment has
            a global context and is accessible from the web ui. Keep in mind only to provide one of
            the four context. You can't attach a file to several context in one request. A error is
            thrown if you provide two or more context (i. E. sending customer_id, document_id and
            project_id in combination).

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, Attachment]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
