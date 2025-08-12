# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountRetrieveRecordingsJsonParams"]


class AccountRetrieveRecordingsJsonParams(TypedDict, total=False):
    date_created: Annotated[Union[str, datetime], PropertyInfo(alias="DateCreated", format="iso8601")]
    """Filters recording by the creation date.

    Expected format is ISO8601 date or date-time, ie. {YYYY}-{MM}-{DD} or
    {YYYY}-{MM}-{DD}T{hh}:{mm}:{ss}Z. Also accepts inequality operators, e.g.
    DateCreated>=2023-05-22.
    """

    page: Annotated[int, PropertyInfo(alias="Page")]
    """
    The number of the page to be displayed, zero-indexed, should be used in
    conjuction with PageToken.
    """

    page_size: Annotated[int, PropertyInfo(alias="PageSize")]
    """The number of records to be displayed on a page"""
