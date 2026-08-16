# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["ActionQueryResponse", "Data", "DataMeta"]


class DataMeta(BaseModel):
    changes: Optional[int] = None
    """Number of rows added, changed, or removed by the statement."""

    duration: Optional[float] = None
    """Wall-clock duration of the statement, in milliseconds."""

    last_row_id: Optional[int] = None
    """Rowid of the last inserted row, when applicable."""

    rows_read: Optional[int] = None

    rows_written: Optional[int] = None


class Data(BaseModel):
    count: Optional[int] = None
    """Number of rows returned."""

    duration: Optional[float] = None
    """Wall-clock duration of the request, in milliseconds."""

    meta: Optional[DataMeta] = None

    results: Optional[List[Dict[str, object]]] = None
    """The result rows, each a map of column name to value.

    Empty for statements that return no rows.
    """

    success: Optional[bool] = None


class ActionQueryResponse(BaseModel):
    data: Optional[Data] = None
