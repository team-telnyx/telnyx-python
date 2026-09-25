# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._models import BaseModel

__all__ = ["ProfileDeleteResponse", "Data"]


class Data(BaseModel):
    memories_deleted: int
    """Memories the profile held and no longer does, counted before and after.

    A report rather than an audit: memory moves in the background between the two
    counts. The status carries the outcome.
    """

    profile_id: str


class ProfileDeleteResponse(BaseModel):
    data: Data
