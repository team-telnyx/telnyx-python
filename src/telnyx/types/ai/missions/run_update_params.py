# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .run_status import RunStatus

__all__ = ["RunUpdateParams"]


class RunUpdateParams(TypedDict, total=False):
    mission_id: Required[str]

    error: str

    metadata: Dict[str, object]

    result_payload: Dict[str, object]

    result_summary: str

    status: RunStatus
