# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .recording_response_data import RecordingResponseData

__all__ = ["RecordingRetrieveResponse"]


class RecordingRetrieveResponse(BaseModel):
    data: Optional[RecordingResponseData] = None
