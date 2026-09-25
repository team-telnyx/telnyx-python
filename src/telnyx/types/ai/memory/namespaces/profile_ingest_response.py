# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ....._models import BaseModel

__all__ = ["ProfileIngestResponse", "Data"]


class Data(BaseModel):
    operation_id: str

    profile_id: str

    session_id: str

    source_id: str
    """
    Identifies one source within its profile: an ingested session, or one remembered
    fact. Returned by `ingest` and `remember` when the write is accepted.
    Re-ingesting a session keeps its source id.
    """


class ProfileIngestResponse(BaseModel):
    data: Data
