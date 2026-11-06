# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ....._models import BaseModel
from .summary_settings import SummarySettings

__all__ = ["NamespaceSettings"]


class NamespaceSettings(BaseModel):
    """A namespace's settings, grouped by what they affect."""

    summary: Optional[SummarySettings] = None
    """Settings that shape this namespace's summaries."""
