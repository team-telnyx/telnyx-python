# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo
from .tf_verification_status import TfVerificationStatus

__all__ = ["RequestListParams"]


class RequestListParams(TypedDict, total=False):
    page: Required[int]

    page_size: Required[int]
    """Request this many records per page

            This value is automatically clamped if the provided value is too large.
    """

    date_end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    date_start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    phone_number: str

    status: TfVerificationStatus
    """Tollfree verification status"""
