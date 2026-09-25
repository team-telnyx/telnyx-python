# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ....._models import BaseModel

__all__ = ["ProfileRecallResponse", "Data"]


class Data(BaseModel):
    id: str

    text: str

    recorded_at: Optional[str] = None

    score: Optional[float] = None
    """Relevance, 0-1.

    Null where the deployment's reranker is a passthrough; results are in rank order
    either way.
    """


class ProfileRecallResponse(BaseModel):
    data: List[Data]
