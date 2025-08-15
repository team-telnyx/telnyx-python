# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountRetrieveTranscriptionsJsonParams"]


class AccountRetrieveTranscriptionsJsonParams(TypedDict, total=False):
    page_size: Annotated[int, PropertyInfo(alias="PageSize")]
    """The number of records to be displayed on a page"""

    page_token: Annotated[str, PropertyInfo(alias="PageToken")]
    """Used to request the next page of results."""
