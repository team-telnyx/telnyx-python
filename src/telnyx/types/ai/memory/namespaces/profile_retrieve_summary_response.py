# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ....._models import BaseModel

__all__ = ["ProfileRetrieveSummaryResponse", "Data"]


class Data(BaseModel):
    is_stale: bool
    """Whether newer memories have arrived since the summary was generated.

    The summary is regenerated in the background, so a true here is ordinary and the
    summary is still usable.
    """

    profile_id: str

    generated_at: Optional[str] = None
    """When the summary was last generated. Null while none is ready."""

    text: Optional[str] = None
    """
    The precomputed summary, ready to place in an assistant's context at the start
    of a session.
    """


class ProfileRetrieveSummaryResponse(BaseModel):
    data: Data
