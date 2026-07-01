# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .run_status import RunStatus as RunStatus
from .run_list_params import RunListParams as RunListParams
from .run_create_params import RunCreateParams as RunCreateParams
from .run_update_params import RunUpdateParams as RunUpdateParams
from .run_list_runs_params import RunListRunsParams as RunListRunsParams

if TYPE_CHECKING:
    from .mission_run_data import MissionRunData as MissionRunData
    from .mission_run_response import MissionRunResponse as MissionRunResponse
    from .mission_runs_list_response import MissionRunsListResponse as MissionRunsListResponse


def __getattr__(name: str) -> Any:
    if name == "MissionRunData":
        from .mission_run_data import MissionRunData

        return MissionRunData
    if name == "MissionRunResponse":
        from .mission_run_response import MissionRunResponse

        return MissionRunResponse
    if name == "MissionRunsListResponse":
        from .mission_runs_list_response import MissionRunsListResponse

        return MissionRunsListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
