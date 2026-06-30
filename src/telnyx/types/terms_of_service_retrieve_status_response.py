# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from datetime import datetime

from .._models import BaseModel
from .terms_of_service.tos_product_type import TosProductType

__all__ = ["TermsOfServiceRetrieveStatusResponse", "Data"]


class Data(BaseModel):
    """Whether the calling user has agreed to a product's current Terms of Service.

    The `user_id` is intentionally omitted on this public surface.
    """

    agreement_required: bool
    """`true` when the user must agree to the latest version before using the product.

    Equivalent to `!has_agreed`.
    """

    current_terms_version: str
    """Latest published version of the ToS for this product."""

    has_agreed: bool
    """`true` if the user has agreed to the latest version."""

    product_type: TosProductType
    """Telnyx product the Terms of Service apply to."""

    agreed_at: Optional[datetime] = None

    agreed_version: Optional[str] = None
    """
    Version the user previously agreed to (may be older than
    `current_terms_version`). `null` if the user has never agreed.
    """


class TermsOfServiceRetrieveStatusResponse(BaseModel):
    data: Data
    """Whether the calling user has agreed to a product's current Terms of Service.

    The `user_id` is intentionally omitted on this public surface.
    """
