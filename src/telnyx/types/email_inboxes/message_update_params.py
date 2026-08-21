# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["MessageUpdateParams"]


class MessageUpdateParams(TypedDict, total=False):
    inbox_id: Required[str]

    read_at: Required[Annotated[Union[Literal[True], Union[str, datetime]], PropertyInfo(format="iso8601")]]
