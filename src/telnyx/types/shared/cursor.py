# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Cursor"]


class Cursor(BaseModel):
    after: Optional[str] = None
    """Opaque identifier of next page."""

    before: Optional[str] = None
    """Opaque identifier of previous page."""
