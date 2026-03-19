# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrafficPolicyProfileListServicesParams"]


class TrafficPolicyProfileListServicesParams(TypedDict, total=False):
    filter_group: Annotated[str, PropertyInfo(alias="filter[group]")]
    """Filter services by group."""

    filter_name: Annotated[str, PropertyInfo(alias="filter[name]")]
    """Filter services by name."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page."""
