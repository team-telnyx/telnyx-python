# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CloudfListParams"]


class CloudfListParams(TypedDict, total=False):
    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """Return only the filesystem whose name matches exactly."""

    filter_region: Annotated[str, PropertyInfo(alias="filter[region]")]
    """Return only filesystems in this region."""

    filter_status: Annotated[
        Literal["provisioning", "ready", "needs_format", "deleting", "failed"], PropertyInfo(alias="filter[status]")
    ]
    """Return only filesystems with this status. Unrecognized values are ignored."""

    page_after: Annotated[str, PropertyInfo(alias="page[after]")]
    """
    Opaque cursor from a previous response's `meta.cursors.after`; returns the page
    after it. Mutually exclusive with `page[before]`.
    """

    page_before: Annotated[str, PropertyInfo(alias="page[before]")]
    """
    Opaque cursor from a previous response's `meta.cursors.before`; returns the page
    before it. Mutually exclusive with `page[after]`.
    """

    page_limit: Annotated[int, PropertyInfo(alias="page[limit]")]
    """The number of filesystems to return per page.

    Values above 250 are treated as 250.
    """

    sort: Literal["created_at", "-created_at", "updated_at", "-updated_at", "name", "-name"]
    """
    Sort order for the results: a field name for ascending, or the field name
    prefixed with `-` for descending.
    """
