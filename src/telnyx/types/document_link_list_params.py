# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentLinkListParams", "Filter"]


class DocumentLinkListParams(TypedDict, total=False):
    filter: Filter
    """Consolidated filter parameter for document links (deepObject style).

    Originally: filter[linked_record_type], filter[linked_resource_id]
    """

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]


class Filter(TypedDict, total=False):
    """Consolidated filter parameter for document links (deepObject style).

    Originally: filter[linked_record_type], filter[linked_resource_id]
    """

    linked_record_type: str
    """The linked_record_type of the document to filter on."""

    linked_resource_id: str
    """The linked_resource_id of the document to filter on."""
