# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TunnelListParams", "Filter", "Page"]


class TunnelListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style).

    Originally: filter[name], filter[status]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[after], page[limit]
    """

    sort: Literal["name", "-name", "status", "-status", "created_at", "-created_at", "updated_at", "-updated_at"]
    """Sorts the results by a field, ascending, or descending with a leading `-`.

    The default is `-created_at`.
    """


class Filter(TypedDict, total=False):
    """Consolidated filter parameter (deepObject style).

    Originally: filter[name], filter[status]
    """

    name: str
    """The name of the tunnel."""

    status: Literal["inactive", "healthy", "degraded"]
    """The status of the tunnel."""


class Page(TypedDict, total=False):
    """Consolidated page parameter (deepObject style).

    Originally: page[after], page[limit]
    """

    after: str
    """The cursor from `meta.cursors.after` of the previous page."""

    limit: int
    """The number of results per page."""
