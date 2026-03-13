# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TemplateListParams"]


class TemplateListParams(TypedDict, total=False):
    filter_category: Annotated[
        Literal["MARKETING", "UTILITY", "AUTHENTICATION"], PropertyInfo(alias="filter[category]")
    ]
    """Filter by category"""

    filter_search: Annotated[str, PropertyInfo(alias="filter[search]")]
    """Search templates by name"""

    filter_status: Annotated[str, PropertyInfo(alias="filter[status]")]
    """Filter by template status"""

    filter_waba_id: Annotated[str, PropertyInfo(alias="filter[waba_id]")]
    """Filter by WABA ID"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
