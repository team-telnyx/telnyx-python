# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SubNumberOrderRetrieveResponse", "Data", "DataFieldsRequired", "DataRequirementAction"]


class DataFieldsRequired(BaseModel):
    description: Optional[str] = None

    name: Optional[str] = None
    """The field name to send inside the `requirement` object on the POST."""

    type: Optional[str] = None

    value: Optional[str] = None
    """The value already stored for this field, or null if not yet provided."""


class DataRequirementAction(BaseModel):
    type: Optional[str] = None
    """The type of action the end user must complete."""

    value: Optional[str] = None
    """The action value.

    For ID verification this is the verification link URL, or null until it has been
    generated.
    """


class Data(BaseModel):
    fields_required: Optional[List[DataFieldsRequired]] = None
    """The fields the end user must provide to fulfill this requirement."""

    regulatory_requirement_id: Optional[str] = None

    requirement_action: Optional[DataRequirementAction] = None


class SubNumberOrderRetrieveResponse(BaseModel):
    data: Optional[Data] = None
