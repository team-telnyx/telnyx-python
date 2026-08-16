# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from ..._models import BaseModel
from .sql_database import SqlDatabase

__all__ = ["SqlDatabaseResponseWrapper"]


class SqlDatabaseResponseWrapper(BaseModel):
    data: Optional[SqlDatabase] = None
