# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["TestSuiteListResponse"]


class TestSuiteListResponse(BaseModel):
    __test__ = False
    data: List[str]
    """Array of unique test suite names available to the user."""
