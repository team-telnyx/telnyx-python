# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ......_models import BaseModel

__all__ = ["MemoryListResponse"]


class MemoryListResponse(BaseModel):
    id: str

    source_id: Optional[str] = None
    """The source this memory was extracted from.

    Set for a fact, which comes from exactly one source; null for a memory derived
    from other memories. Read it with `GET .../sources/{source_id}`. A source
    deleted a moment ago can still be named here, and then answers 404.
    """

    text: str

    recorded_at: Optional[str] = None
