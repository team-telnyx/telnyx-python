# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["DocumentLinkListParams", "Filter", "Page"]


class DocumentLinkListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for document links (deepObject style).

    Originally: filter[linked_record_type], filter[linked_resource_id]
    """

    page: Page
    """Consolidated page parameter (deepObject style).

    Originally: page[size], page[number]
    """


class Filter(TypedDict, total=False):
    linked_record_type: str
    """The linked_record_type of the document to filter on."""

    linked_resource_id: str
    """The linked_resource_id of the document to filter on."""


class Page(TypedDict, total=False):
    number: int
    """The page number to load"""

    size: int
    """The size of the page"""
