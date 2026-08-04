# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .email_domain_type import EmailDomainType
from .email_domain_status import EmailDomainStatus

__all__ = ["EmailDomainListParams"]


class EmailDomainListParams(TypedDict, total=False):
    filter_domain: Annotated[str, PropertyInfo(alias="filter[domain]")]
    """Partial match on domain name (case-insensitive)"""

    filter_profile_id: Annotated[str, PropertyInfo(alias="filter[profile_id]")]
    """Filter by profile UUID"""

    filter_status: Annotated[EmailDomainStatus, PropertyInfo(alias="filter[status]")]

    filter_type: Annotated[EmailDomainType, PropertyInfo(alias="filter[type]")]

    filter_usable_for_inbound: Annotated[bool, PropertyInfo(alias="filter[usable_for_inbound]")]

    filter_usable_for_sending: Annotated[bool, PropertyInfo(alias="filter[usable_for_sending]")]

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """Cursor for records after the provided value (cursor pagination)"""

    page_before: Annotated[str, PropertyInfo(alias="page[before]")]
    """Cursor for records before the provided value (cursor pagination)"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """Page number to return (offset pagination)"""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Number of records per page"""

    sort: Literal["created_at", "-created_at", "domain", "-domain"]
    """Field to sort by. Prefix with `-` for descending order."""
