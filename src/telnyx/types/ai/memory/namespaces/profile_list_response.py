# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._models import BaseModel

__all__ = ["ProfileListResponse"]


class ProfileListResponse(BaseModel):
    memory_count: int
    """
    Memories stored under this profile, including the consolidated ones that
    paraphrase others. Listings are ordered by it.
    """

    profile_id: str
