# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .background_task_status import BackgroundTaskStatus

__all__ = ["EmbeddingListResponse", "Data"]


class Data(BaseModel):
    created_at: datetime

    status: BackgroundTaskStatus
    """Status of an embeddings task."""

    task_id: str

    task_name: str

    user_id: str

    bucket: Optional[str] = None

    finished_at: Optional[datetime] = None


class EmbeddingListResponse(BaseModel):
    data: List[Data]
