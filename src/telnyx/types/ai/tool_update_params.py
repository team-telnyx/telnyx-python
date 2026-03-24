# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    display_name: str

    function: Dict[str, object]

    handoff: Dict[str, object]

    invite: Dict[str, object]

    retrieval: Dict[str, object]

    timeout_ms: int

    type: str

    webhook: Dict[str, object]
