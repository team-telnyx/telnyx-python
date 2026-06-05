# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TermsOfServiceStatusResponse", "Data"]


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

    product_type: Literal["branded_calling", "number_reputation"]
    """Telnyx product the Terms of Service apply to."""

    agreed_at: Optional[datetime] = None

    agreed_version: Optional[str] = None
    """
    Version the user previously agreed to (may be older than
    `current_terms_version`). `null` if the user has never agreed.
    """


class TermsOfServiceStatusResponse(BaseModel):
    data: Data
    """Whether the calling user has agreed to a product's current Terms of Service.

    The `user_id` is intentionally omitted on this public surface.
    """
