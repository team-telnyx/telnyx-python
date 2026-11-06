# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._models import BaseModel
from .external_verification import ExternalVerification

__all__ = ["ExternalVerificationWrapped"]


class ExternalVerificationWrapped(BaseModel):
    data: ExternalVerification
