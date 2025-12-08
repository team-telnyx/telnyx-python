# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .meta import Meta
from ......_models import BaseModel
from ..test_run_response import TestRunResponse

__all__ = ["PaginatedTestRunList"]


class PaginatedTestRunList(BaseModel):
    """Paginated list of test runs with metadata.

    Returns test run execution results with pagination support for
    handling large numbers of test executions.
    """

    data: List[TestRunResponse]
    """Array of test run objects for the current page."""

    meta: Meta
    """Pagination metadata including total counts and current page info."""
