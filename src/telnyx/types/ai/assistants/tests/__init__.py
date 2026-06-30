# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .test_status import TestStatus as TestStatus
from .run_list_params import RunListParams as RunListParams
from .run_trigger_params import RunTriggerParams as RunTriggerParams

if TYPE_CHECKING:
    from .test_run_response import TestRunResponse as TestRunResponse
    from .test_run_detail_result import TestRunDetailResult as TestRunDetailResult
    from .test_suite_list_response import TestSuiteListResponse as TestSuiteListResponse


def __getattr__(name: str) -> Any:
    if name == "TestSuiteListResponse":
        from .test_suite_list_response import TestSuiteListResponse

        return TestSuiteListResponse
    if name == "TestRunDetailResult":
        from .test_run_detail_result import TestRunDetailResult

        return TestRunDetailResult
    if name == "TestRunResponse":
        from .test_run_response import TestRunResponse

        return TestRunResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
