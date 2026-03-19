# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TrafficPolicyProfileListParams"]


class TrafficPolicyProfileListParams(TypedDict, total=False):
    filter_service: Annotated[str, PropertyInfo(alias="filter[service]")]
    """Filter by service ID."""

    filter_type: Annotated[Literal["whitelist", "blacklist", "throttling"], PropertyInfo(alias="filter[type]")]
    """Filter by traffic policy profile type."""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """The page number to load."""

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """The size of the page."""

    sort: Literal["service", "-service", "type", "-type"]
    """Sorts traffic policy profiles by the given field.

    Defaults to ascending order unless field is prefixed with a minus sign.
    """
