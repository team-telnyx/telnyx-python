# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ListObjectsResponse", "Content"]


class Content(BaseModel):
    key: Optional[str] = FieldInfo(alias="Key", default=None)

    last_modified: Optional[datetime] = FieldInfo(alias="LastModified", default=None)

    size: Optional[float] = FieldInfo(alias="Size", default=None)


class ListObjectsResponse(BaseModel):
    contents: Optional[List[Content]] = FieldInfo(alias="Contents", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)
