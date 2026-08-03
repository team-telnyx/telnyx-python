# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["FilterDeleteAllResponse", "Data"]


class Data(BaseModel):
    allowlist: List[str]

    blocklist: List[str]

    record_type: Literal["email_inbox_filters"]


class FilterDeleteAllResponse(BaseModel):
    data: Data
