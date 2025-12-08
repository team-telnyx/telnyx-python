# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Filter"]


class Filter(BaseModel):
    """Query filter criteria.

    Note: The first filter object must specify filter_type as 'and'. You cannot follow an 'or' with another 'and'.
    """

    billing_group: Optional[str] = None
    """Billing group UUID to filter by"""

    cld: Optional[str] = None
    """Called line identification (destination number)"""

    cld_filter: Optional[Literal["contains", "starts_with", "ends_with"]] = None
    """Filter type for CLD matching"""

    cli: Optional[str] = None
    """Calling line identification (caller ID)"""

    cli_filter: Optional[Literal["contains", "starts_with", "ends_with"]] = None
    """Filter type for CLI matching"""

    filter_type: Optional[Literal["and", "or"]] = None
    """Logical operator for combining filters"""

    tags_list: Optional[str] = None
    """Tag name to filter by"""
