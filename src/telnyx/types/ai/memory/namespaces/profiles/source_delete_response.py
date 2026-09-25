# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ......_models import BaseModel

__all__ = ["SourceDeleteResponse", "Data"]


class Data(BaseModel):
    memories_deleted: int
    """
    Memories the profile held and no longer does, counted before and after across
    the whole profile: it includes memories derived from this source together with
    others, and anything else the profile lost in between. A report rather than an
    audit. The status carries the outcome.
    """

    profile_id: str

    source_id: str
    """
    Identifies one source within its profile: an ingested session, or one remembered
    fact. Returned by `ingest` and `remember` when the write is accepted.
    Re-ingesting a session keeps its source id.
    """


class SourceDeleteResponse(BaseModel):
    data: Data
