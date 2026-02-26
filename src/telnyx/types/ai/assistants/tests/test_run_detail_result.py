# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel
from .test_status import TestStatus

__all__ = ["TestRunDetailResult"]


class TestRunDetailResult(BaseModel):
    __test__ = False
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
