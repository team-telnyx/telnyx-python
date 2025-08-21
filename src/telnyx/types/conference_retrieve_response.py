# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .conference import Conference

__all__ = ["ConferenceRetrieveResponse"]


class ConferenceRetrieveResponse(BaseModel):
    data: Optional[Conference] = None
