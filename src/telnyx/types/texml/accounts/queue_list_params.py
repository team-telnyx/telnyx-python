# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["QueueListParams"]


class QueueListParams(TypedDict, total=False):
    date_created: Annotated[str, PropertyInfo(alias="DateCreated")]
    """Filters conferences by the creation date.

    Expected format is YYYY-MM-DD. Also accepts inequality operators, e.g.
    DateCreated>=2023-05-22.
    """

    date_updated: Annotated[str, PropertyInfo(alias="DateUpdated")]
    """Filters conferences by the time they were last updated.

    Expected format is YYYY-MM-DD. Also accepts inequality operators, e.g.
    DateUpdated>=2023-05-22.
    """

    page: Annotated[int, PropertyInfo(alias="Page")]
    """
    The number of the page to be displayed, zero-indexed, should be used in
    conjuction with PageToken.
    """

    page_size: Annotated[int, PropertyInfo(alias="PageSize")]
    """The number of records to be displayed on a page"""

    page_token: Annotated[str, PropertyInfo(alias="PageToken")]
    """Used to request the next page of results."""
