# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TermsOfServiceInfoResponse", "Agreement"]


class Agreement(BaseModel):
    current_version: Optional[str] = None

    description: Optional[str] = None

    effective_date: Optional[date] = None

    product_type: Optional[Literal["branded_calling", "number_reputation"]] = None
    """Telnyx product the Terms of Service apply to."""

    terms_url: Optional[str] = None


class TermsOfServiceInfoResponse(BaseModel):
    agreements: Optional[List[Agreement]] = None
