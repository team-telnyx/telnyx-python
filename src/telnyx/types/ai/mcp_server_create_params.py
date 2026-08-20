# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["McpServerCreateParams"]


class McpServerCreateParams(TypedDict, total=False):
    name: Required[str]

    type: Required[str]

    url: Required[str]

    allowed_tools: Optional[SequenceNotStr[str]]

    api_key_ref: Optional[str]

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
