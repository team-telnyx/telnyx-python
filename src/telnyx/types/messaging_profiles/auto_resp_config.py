# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AutoRespConfig"]


class AutoRespConfig(BaseModel):
    id: str

    country_code: str

    created_at: datetime

    keywords: List[str]

    op: Literal["start", "stop", "info"]

    updated_at: datetime

    resp_text: Optional[str] = None
