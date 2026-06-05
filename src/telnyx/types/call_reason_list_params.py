# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CallReasonListParams"]


class CallReasonListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]
    """1-based page number.

    Out-of-range values return an empty page with correct meta.
    """

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]
    """Items per page.

    Default `100` for this endpoint (the call-reason library is small and most
    callers want the whole list in one call). Maximum 250; values above are clamped
    to 250.
    """
