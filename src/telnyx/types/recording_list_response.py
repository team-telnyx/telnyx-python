# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .pagination_meta import PaginationMeta
from .recording_response_data import RecordingResponseData

__all__ = ["RecordingListResponse"]


class RecordingListResponse(BaseModel):
    data: Optional[List[RecordingResponseData]] = None

    meta: Optional[PaginationMeta] = None
