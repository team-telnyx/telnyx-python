# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExternalConnectionListParams", "Filter", "FilterConnectionName", "FilterPhoneNumber"]


class ExternalConnectionListParams(TypedDict, total=False):
    filter: Filter
    """Filter parameter for external connections (deepObject style).

    Supports filtering by connection_name, external_sip_connection, id, created_at,
    and phone_number.
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class FilterConnectionName(TypedDict, total=False):
    contains: str
    """
    If present, connections with <code>connection_name</code> containing the given
    value will be returned. Matching is not case-sensitive. Requires at least three
    characters.
    """


class FilterPhoneNumber(TypedDict, total=False):
    """Phone number filter for connections.

    Note: Despite the 'contains' name, this requires a full E164 match per the original specification.
    """

    contains: str
    """If present, connections associated with the given phone_number will be returned.

    A full match is necessary with a e164 format.
    """


class Filter(TypedDict, total=False):
    """Filter parameter for external connections (deepObject style).

    Supports filtering by connection_name, external_sip_connection, id, created_at, and phone_number.
    """

    id: str
    """
    If present, connections with <code>id</code> matching the given value will be
    returned.
    """

    connection_name: FilterConnectionName

    created_at: str
    """
    If present, connections with <code>created_at</code> date matching the given
    YYYY-MM-DD date will be returned.
    """

    external_sip_connection: Literal["zoom", "operator_connect"]
    """
    If present, connections with <code>external_sip_connection</code> matching the
    given value will be returned.
    """

    phone_number: FilterPhoneNumber
    """Phone number filter for connections.

    Note: Despite the 'contains' name, this requires a full E164 match per the
    original specification.
    """
