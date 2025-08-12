# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ....._models import BaseModel
from .test_status import TestStatus

__all__ = ["TestRunResponse", "DetailStatus"]


class DetailStatus(BaseModel):
    name: str

    status: TestStatus
    """Represents the lifecycle of a test:

    - 'pending': Test is waiting to be executed.
    - 'starting': Test execution is initializing.
    - 'running': Test is currently executing.
    - 'passed': Test completed successfully.
    - 'failed': Test executed but did not pass.
    - 'error': An error occurred during test execution.
    """


class TestRunResponse(BaseModel):
    __test__ = False
    created_at: datetime
    """Timestamp when the test run was created and queued."""

    run_id: str
    """Unique identifier for this specific test run execution."""

    status: TestStatus
    """Represents the lifecycle of a test:

    - 'pending': Test is waiting to be executed.
    - 'starting': Test execution is initializing.
    - 'running': Test is currently executing.
    - 'passed': Test completed successfully.
    - 'failed': Test executed but did not pass.
    - 'error': An error occurred during test execution.
    """

    test_id: str
    """Identifier of the assistant test that was executed."""

    triggered_by: str
    """How this test run was initiated (manual, scheduled, or API)."""

    completed_at: Optional[datetime] = None
    """Timestamp when the test run finished execution."""

    conversation_id: Optional[str] = None
    """Identifier of the conversation created during test execution."""

    conversation_insights_id: Optional[str] = None
    """Identifier for conversation analysis and insights data."""

    detail_status: Optional[List[DetailStatus]] = None
    """Detailed evaluation results for each rubric criteria.

    Name is name of the criteria from the rubric and status is the result of the
    evaluation. This list will have a result for every criteria in the rubric
    section.
    """

    logs: Optional[str] = None
    """Detailed execution logs and debug information."""

    test_suite_run_id: Optional[str] = None
    """Identifier linking this run to a test suite execution batch."""

    updated_at: Optional[datetime] = None
    """Timestamp of the last update to this test run."""
