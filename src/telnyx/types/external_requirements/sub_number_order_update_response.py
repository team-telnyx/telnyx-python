# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel

__all__ = ["SubNumberOrderUpdateResponse", "Data", "DataRequirementAction"]


class DataRequirementAction(BaseModel):
    type: Optional[str] = None

    value: Optional[str] = None
    """
    For Australia mobile ID verification, the unique Onfido verification link to
    share with the end user.
    """


class Data(BaseModel):
    regulatory_requirement_id: Optional[str] = None

    requirement_action: Optional[DataRequirementAction] = None

    sub_order_id: Optional[str] = None


class SubNumberOrderUpdateResponse(BaseModel):
    data: Optional[Data] = None
