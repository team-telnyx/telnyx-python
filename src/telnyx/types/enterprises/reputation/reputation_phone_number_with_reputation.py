# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._models import BaseModel
from .reputation_phone_number import ReputationPhoneNumber

__all__ = ["ReputationPhoneNumberWithReputation"]


class ReputationPhoneNumberWithReputation(BaseModel):
    data: ReputationPhoneNumber
