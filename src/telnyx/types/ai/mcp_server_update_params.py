# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["McpServerUpdateParams"]


class McpServerUpdateParams(TypedDict, total=False):
    id: str

    allowed_tools: Optional[SequenceNotStr[str]]

    api_key_ref: Optional[str]

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    name: str

    type: str

    url: str
