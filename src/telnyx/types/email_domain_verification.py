# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmailDomainVerification"]


class EmailDomainVerification(BaseModel):
    dkim: Literal["pending", "verified", "failed"]

    dmarc: Literal["missing_optional", "verified", "failed"]

    mx: Literal["not_required", "pending", "verified", "failed"]

    ownership: Literal["pending", "verified", "not_required"]

    spf: Literal["missing_optional", "verified", "failed", "not_required"]
