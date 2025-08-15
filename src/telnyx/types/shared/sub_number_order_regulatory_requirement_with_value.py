# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubNumberOrderRegulatoryRequirementWithValue"]


class SubNumberOrderRegulatoryRequirementWithValue(BaseModel):
    field_type: Optional[Literal["textual", "datetime", "address", "document"]] = None

    field_value: Optional[str] = None
    """
    The value of the requirement, this could be an id to a resource or a string
    value.
    """

    record_type: Optional[str] = None

    requirement_id: Optional[str] = None
    """Unique id for a requirement."""
