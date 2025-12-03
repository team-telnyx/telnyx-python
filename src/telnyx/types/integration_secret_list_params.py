# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["IntegrationSecretListParams", "Filter", "Page"]


class IntegrationSecretListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter (deepObject style). Originally: filter[type]"""

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class Filter(TypedDict, total=False):
    type: Literal["bearer", "basic"]


class Page(TypedDict, total=False):
    number: int

    size: int
