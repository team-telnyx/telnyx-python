# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SimCardActionsSummary"]


class SimCardActionsSummary(BaseModel):
    count: Optional[int] = None

    status: Optional[Literal["in-progress", "completed", "failed", "interrupted"]] = None
