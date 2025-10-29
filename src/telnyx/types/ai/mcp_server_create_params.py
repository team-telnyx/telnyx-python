# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["McpServerCreateParams"]


class McpServerCreateParams(TypedDict, total=False):
    name: Required[str]

    type: Required[str]

    url: Required[str]

    allowed_tools: Optional[SequenceNotStr[str]]

    api_key_ref: Optional[str]
