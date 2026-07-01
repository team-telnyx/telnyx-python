# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypeAlias

__all__ = ["CommentType"]

CommentType: TypeAlias = Literal[
    "vetting_comment",
    "rejection_reason",
    "internal_note",
    "notification",
    "status_update",
    "customer_inquiry",
    "admin_response",
]
