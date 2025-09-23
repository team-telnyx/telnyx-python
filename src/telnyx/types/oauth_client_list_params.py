# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["OAuthClientListParams"]


class OAuthClientListParams(TypedDict, total=False):
    filter_allowed_grant_types_contains: Annotated[
        Literal["client_credentials", "authorization_code", "refresh_token"],
        PropertyInfo(alias="filter[allowed_grant_types][contains]"),
    ]
    """Filter by allowed grant type"""

    filter_client_id: Annotated[str, PropertyInfo(alias="filter[client_id]")]
    """Filter by client ID"""

    filter_client_type: Annotated[Literal["confidential", "public"], PropertyInfo(alias="filter[client_type]")]
    """Filter by client type"""

    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """Filter by exact client name"""

    filter_name_contains: Annotated[str, PropertyInfo(alias="filter[name][contains]")]
    """Filter by client name containing text"""

    filter_verified: Annotated[bool, PropertyInfo(alias="filter[verified]")]
    """Filter by verification status"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number"""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of results per page"""
