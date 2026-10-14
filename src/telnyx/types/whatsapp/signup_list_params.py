# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SignupListParams"]


class SignupListParams(TypedDict, total=False):
    filter_created_at_gte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[created_at][gte]", format="iso8601")
    ]
    """Return sessions created at or after this time (RFC 3339)"""

    filter_created_at_lte: Annotated[
        Union[str, datetime], PropertyInfo(alias="filter[created_at][lte]", format="iso8601")
    ]
    """Return sessions created at or before this time (RFC 3339)"""

    filter_customer_id: Annotated[str, PropertyInfo(alias="filter[customer_id]")]
    """Filter by the tech provider customer reference"""

    filter_waba_id: Annotated[str, PropertyInfo(alias="filter[waba_id]")]
    """Filter by Meta WABA ID"""

    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
