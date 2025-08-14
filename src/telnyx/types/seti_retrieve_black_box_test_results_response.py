# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SetiRetrieveBlackBoxTestResultsResponse", "Data", "DataBlackBoxTest"]


class DataBlackBoxTest(BaseModel):
    id: Optional[str] = None
    """The name of the black box test."""

    record_type: Optional[str] = None

    result: Optional[float] = None
    """The average result of the black box test over the last hour."""


class Data(BaseModel):
    black_box_tests: Optional[List[DataBlackBoxTest]] = None

    product: Optional[str] = None
    """The product associated with the black box test group."""

    record_type: Optional[str] = None


class SetiRetrieveBlackBoxTestResultsResponse(BaseModel):
    data: Optional[List[Data]] = None
