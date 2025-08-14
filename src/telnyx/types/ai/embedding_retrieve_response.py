# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .background_task_status import BackgroundTaskStatus

__all__ = ["EmbeddingRetrieveResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[str] = None

    finished_at: Optional[str] = None

    status: Optional[BackgroundTaskStatus] = None
    """Status of an embeddings task."""

    task_id: Optional[str] = None

    task_name: Optional[str] = None


class EmbeddingRetrieveResponse(BaseModel):
    data: Data
