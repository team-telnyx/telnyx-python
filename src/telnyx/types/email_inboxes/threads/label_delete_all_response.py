# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["LabelDeleteAllResponse", "Data"]


class Data(BaseModel):
    id: str

    labels: List[str]

    record_type: Literal["email_thread"]

    inbox_id: Optional[str] = None


class LabelDeleteAllResponse(BaseModel):
    data: Data
