# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .run_list_params import RunListParams as RunListParams
from .run_trigger_params import RunTriggerParams as RunTriggerParams
from .run_trigger_response import RunTriggerResponse as RunTriggerResponse

if TYPE_CHECKING:
    from .meta import Meta as Meta
    from .paginated_test_run_list import PaginatedTestRunList as PaginatedTestRunList


def __getattr__(name: str) -> Any:
    if name == "Meta":
        from .meta import Meta

        return Meta
    if name == "PaginatedTestRunList":
        from .paginated_test_run_list import PaginatedTestRunList

        return PaginatedTestRunList
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
