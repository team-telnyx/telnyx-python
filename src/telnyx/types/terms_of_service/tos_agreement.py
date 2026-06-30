# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .tos_product_type import TosProductType

__all__ = ["TosAgreement"]


class TosAgreement(BaseModel):
    """A recorded user agreement to a product's Terms of Service.

    The `user_id` is intentionally NOT echoed back on this public surface - the caller already knows their own identity.
    """

    id: Optional[str] = None

    agreed_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    product_type: Optional[TosProductType] = None
    """Telnyx product the Terms of Service apply to."""

    terms_version: Optional[str] = None

    version: Optional[str] = None
    """Convenience alias of `terms_version`. Both keys are present on every response."""
