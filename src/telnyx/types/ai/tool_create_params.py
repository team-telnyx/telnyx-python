# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

from .pay_tool_params_param import PayToolParamsParam

__all__ = ["ToolCreateParams"]


class ToolCreateParams(TypedDict, total=False):
    display_name: Required[str]

    type: Required[str]

    client_side_tool: Dict[str, object]

    function: Dict[str, object]

    handoff: Dict[str, object]

    invite: Dict[str, object]

    pay: PayToolParamsParam

    retrieval: Dict[str, object]

    timeout_ms: int

    webhook: Dict[str, object]
