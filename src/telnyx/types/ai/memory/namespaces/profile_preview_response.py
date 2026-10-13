# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ....._models import BaseModel

__all__ = ["ProfilePreviewResponse", "Data"]


class Data(BaseModel):
    profile_id: str

    text: Optional[str] = None
    """The summary this profile would carry under the candidate note.

    Null when nothing was generated -- the same signal `GET /summary` uses for a
    profile with no card yet.
    """


class ProfilePreviewResponse(BaseModel):
    data: Data
