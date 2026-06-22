# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["DirStatus"]

DirStatus: TypeAlias = Literal[
    "draft",
    "submitted",
    "in_review",
    "verified",
    "rejected",
    "unsuccessful",
    "suspended",
    "expired",
    "infringement_claimed",
    "permanently_rejected",
]
