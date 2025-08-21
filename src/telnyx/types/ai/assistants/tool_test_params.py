# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ToolTestParams"]


class ToolTestParams(TypedDict, total=False):
    assistant_id: Required[str]

    arguments: Dict[str, object]
    """Key-value arguments to use for the webhook test"""

    dynamic_variables: Dict[str, object]
    """Key-value dynamic variables to use for the webhook test"""
