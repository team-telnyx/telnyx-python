# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["EmailDomainStatus"]

EmailDomainStatus: TypeAlias = Literal["pending", "verifying", "verified", "failed", "degraded", "suspended"]
