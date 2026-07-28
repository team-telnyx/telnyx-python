# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from .._models import BaseModel
from .email_inboxes.email_message import EmailMessage

__all__ = ["EmailMessageBatchResponse", "Error", "Meta"]


class Error(BaseModel):
    code: Literal[
        "bad_request",
        "not_found",
        "forbidden",
        "service_unavailable",
        "validation_error",
        "recipient_suppressed",
        "reputation_suspended",
    ]
    """Batch item errors use `message` (not `detail`) for the human-readable text."""

    index: int
    """Zero-based index of the failed message in the request array."""

    message: str


class Meta(BaseModel):
    failed: int

    succeeded: int

    total: int


class EmailMessageBatchResponse(BaseModel):
    data: List[EmailMessage]

    errors: List[Error]

    meta: Meta
