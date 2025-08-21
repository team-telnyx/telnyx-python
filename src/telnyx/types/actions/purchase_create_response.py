# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ..._models import BaseModel
from ..shared.simple_sim_card import SimpleSimCard

__all__ = ["PurchaseCreateResponse", "Error", "ErrorSource"]


class ErrorSource(BaseModel):
    parameter: Optional[str] = None
    """Indicates which query parameter caused the error."""

    pointer: Optional[str] = None
    """JSON pointer (RFC6901) to the offending entity."""


class Error(BaseModel):
    code: str

    title: str

    detail: Optional[str] = None

    meta: Optional[Dict[str, object]] = None

    source: Optional[ErrorSource] = None


class PurchaseCreateResponse(BaseModel):
    data: Optional[List[SimpleSimCard]] = None
    """Successfully registered SIM cards."""

    errors: Optional[List[Error]] = None
