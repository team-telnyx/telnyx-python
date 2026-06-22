# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RejectionReason"]


class RejectionReason(BaseModel):
    code: Optional[str] = None

    detail: Optional[str] = None

    message: Optional[str] = None
    """Customer-visible free-text comment from the Telnyx vetting team.

    Only the first entry of `rejection_reasons` carries this; the rest are `null`.
    """

    title: Optional[str] = None
