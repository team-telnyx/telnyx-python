# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["InsightTemplate"]


class InsightTemplate(BaseModel):
    id: str

    created_at: datetime

    instructions: str

    insight_type: Optional[Literal["custom", "default"]] = None

    json_schema: Union[str, object, None] = None
    """If specified, the output will follow the JSON schema."""

    name: Optional[str] = None

    webhook: Optional[str] = None
