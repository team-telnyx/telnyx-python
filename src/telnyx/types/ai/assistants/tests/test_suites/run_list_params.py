# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ......_utils import PropertyInfo

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    page_number: Annotated[int, PropertyInfo(alias="page[number]")]

    page_size: Annotated[int, PropertyInfo(alias="page[size]")]

    status: str
    """Filter runs by execution status (pending, running, completed, failed, timeout)"""

    test_suite_run_id: str
    """Filter runs by specific suite execution batch ID"""
