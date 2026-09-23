# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .._models import BaseModel

__all__ = ["SuccessResponse"]


class SuccessResponse(BaseModel):
    """Status envelope used by the signup and magic-link flows."""

    message: str
    """Human-readable status message."""

    success: bool
    """Whether the request was accepted."""
