# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .bucket_ids import BucketIDs

__all__ = ["RetrievalTool"]


class RetrievalTool(BaseModel):
    retrieval: BucketIDs

    type: Literal["retrieval"]

    shared: Optional[bool] = None
    """Whether this tool comes from the shared Tools Library.

    Responses merge shared tools into `tools` with `shared: true`; inline tools
    carry `shared: false`. Read-only: set by the server, not accepted in requests.
    When updating an assistant, omit `shared: true` tools from the request `tools`
    array and manage them through `tool_ids` instead — re-sending their definitions
    creates an inline duplicate (rejected with error code 10015 when the type allows
    only one instance per assistant).
    """
