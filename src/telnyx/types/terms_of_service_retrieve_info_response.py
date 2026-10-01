# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from datetime import date

from .._models import BaseModel
from .terms_of_service.tos_product_type import TosProductType

__all__ = ["TermsOfServiceRetrieveInfoResponse", "Agreement"]


class Agreement(BaseModel):
    current_version: Optional[str] = None
    """The latest published version of these terms."""

    description: Optional[str] = None
    """A short summary of the product these terms cover."""

    effective_date: Optional[date] = None
    """The date this version took effect."""

    product_type: Optional[TosProductType] = None
    """Telnyx product the Terms of Service apply to."""

    terms_url: Optional[str] = None
    """A link to the full terms text."""


class TermsOfServiceRetrieveInfoResponse(BaseModel):
    agreements: Optional[List[Agreement]] = None
