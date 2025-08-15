# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SubNumberOrderRegulatoryRequirement"]


class SubNumberOrderRegulatoryRequirement(BaseModel):
    field_type: Optional[Literal["textual", "datetime", "address", "document"]] = None

    record_type: Optional[str] = None

    requirement_id: Optional[str] = None
    """Unique id for a requirement."""
