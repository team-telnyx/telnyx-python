# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ....._models import BaseModel

__all__ = ["TestSuiteListResponse"]


class TestSuiteListResponse(BaseModel):
    __test__ = False
    """Response containing all available test suite names.

    Returns a list of distinct test suite names that can be used for
    filtering and organizing tests.
    """
    data: List[str]
    """Array of unique test suite names available to the user."""
