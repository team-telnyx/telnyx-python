# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UserListParams"]


class UserListParams(TypedDict, total=False):
    filter_email: Annotated[str, PropertyInfo(alias="filter[email]")]
    """Filter by email address (partial match)"""

    filter_user_status: Annotated[Literal["enabled", "disabled", "blocked"], PropertyInfo(alias="filter[user_status]")]
    """Filter by user status"""

    include_groups: bool
    """When set to true, includes the groups array for each user in the response.

    The groups array contains objects with id and name for each group the user
    belongs to.
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load"""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page"""
