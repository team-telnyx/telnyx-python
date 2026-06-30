# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel
from .tos_agreement import TosAgreement

__all__ = ["TosAgreementWrapped"]


class TosAgreementWrapped(BaseModel):
    data: TosAgreement
    """A recorded user agreement to a product's Terms of Service.

    The `user_id` is intentionally NOT echoed back on this public surface - the
    caller already knows their own identity.
    """
