# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._models import BaseModel

__all__ = ["ProductListResponse"]


class ProductListResponse(BaseModel):
    description: str
    """Human-readable description of the product."""

    name: str
    """Display name of the product."""

    slug: str
    """Product identifier used in the per-product pricing endpoint."""
