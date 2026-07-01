# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel
from .infringement_claim import InfringementClaim

__all__ = ["InfringementClaimWrapped"]


class InfringementClaimWrapped(BaseModel):
    data: InfringementClaim
