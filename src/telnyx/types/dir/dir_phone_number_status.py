# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["DirPhoneNumberStatus"]

DirPhoneNumberStatus: TypeAlias = Literal[
    "submitted", "in_review", "verified", "unsuccessful", "suspended", "expired", "permanently_rejected"
]
