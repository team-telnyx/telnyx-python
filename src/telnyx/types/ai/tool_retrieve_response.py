# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["ToolRetrieveResponse"]


class ToolRetrieveResponse(BaseModel):
    id: str

    tool_definition: Dict[str, object]

    type: str

    created_at: Optional[str] = None

    display_name: Optional[str] = None

    timeout_ms: Optional[int] = None
