# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional

from ......_models import BaseModel

__all__ = ["SourceRetrieveResponse", "Data"]


class Data(BaseModel):
    id: str
    """
    Identifies one source within its profile: an ingested session, or one remembered
    fact. Returned by `ingest` and `remember` when the write is accepted.
    Re-ingesting a session keeps its source id.
    """

    content: Union[Dict[str, object], Union[List[object], str, float, bool]]
    """
    What was stored, in the shape it was sent: an ingested JSON body as JSON, a
    string body or a remembered fact as a string. A session ingested before formats
    were recorded is returned as the text it was stored as.
    """

    memory_count: int
    """Memories extracted from this source.

    A memory derived from several sources is not counted here.
    """

    session_id: Optional[str] = None
    """The session this source was ingested as. Null for a remembered fact."""

    created_at: Optional[str] = None
    """When the source was first stored."""

    updated_at: Optional[str] = None
    """When the source was last written; re-ingesting moves it."""


class SourceRetrieveResponse(BaseModel):
    data: Data
