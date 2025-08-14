# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["EmbeddingResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[str] = None

    finished_at: Optional[str] = None

    status: Optional[str] = None

    task_id: Optional[str] = None

    task_name: Optional[str] = None

    user_id: Optional[str] = None


class EmbeddingResponse(BaseModel):
    data: Data
