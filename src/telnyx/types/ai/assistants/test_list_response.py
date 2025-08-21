# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel
from .assistant_test import AssistantTest
from .tests.test_suites.meta import Meta

__all__ = ["TestListResponse"]


class TestListResponse(BaseModel):
    __test__ = False
    data: List[AssistantTest]
    """Array of assistant test objects for the current page."""

    meta: Meta
    """Pagination metadata including total counts and current page info."""
