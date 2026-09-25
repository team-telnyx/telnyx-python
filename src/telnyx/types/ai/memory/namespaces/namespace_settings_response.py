# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ....._models import BaseModel

__all__ = ["NamespaceSettingsResponse", "Data", "DataSummary"]


class DataSummary(BaseModel):
    """Settings that shape this namespace's summaries."""

    instructions: Optional[str] = None
    """
    Free-form instructions that influence how this namespace's summaries are
    written, shared by every profile in the namespace. How you use them is up to you
    -- they steer the outcome, so try a phrasing and see how the summary comes out.
    Advisory: they steer the summary but never override or deny a profile's own
    facts, and they do not affect recall. Null or empty means none are set, and
    summaries use the neutral default. A change reaches each summary the next time
    it is regenerated.
    """


class Data(BaseModel):
    """A namespace's settings, grouped by what they affect."""

    summary: Optional[DataSummary] = None
    """Settings that shape this namespace's summaries."""


class NamespaceSettingsResponse(BaseModel):
    data: Data
    """A namespace's settings, grouped by what they affect."""
