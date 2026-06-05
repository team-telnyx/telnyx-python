# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["NumberRefreshResponse", "Data", "DataResult"]


class DataResult(BaseModel):
    phone_number: str

    success: bool

    error: Optional[str] = None
    """`null` when `success` is `true`; carries an error message otherwise."""


class Data(BaseModel):
    results: List[DataResult]
    """Per-number outcome of the refresh."""

    total_failed: int

    total_requested: int

    total_successful: int


class NumberRefreshResponse(BaseModel):
    data: Data
