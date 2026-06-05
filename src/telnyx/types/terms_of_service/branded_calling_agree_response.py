# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrandedCallingAgreeResponse", "Data"]


class Data(BaseModel):
    """A recorded user agreement to a product's Terms of Service.

    The `user_id` is intentionally NOT echoed back on this public surface — the caller already knows their own identity.
    """

    id: Optional[str] = None

    agreed_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    product_type: Optional[Literal["branded_calling", "number_reputation"]] = None
    """Telnyx product the Terms of Service apply to."""

    terms_version: Optional[str] = None

    version: Optional[str] = None
    """Convenience alias of `terms_version`. Both keys are present on every response."""


class BrandedCallingAgreeResponse(BaseModel):
    data: Data
    """A recorded user agreement to a product's Terms of Service.

    The `user_id` is intentionally NOT echoed back on this public surface — the
    caller already knows their own identity.
    """
