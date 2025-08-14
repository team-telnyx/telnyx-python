# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ListBucketsResponse", "Bucket"]


class Bucket(BaseModel):
    creation_date: Optional[datetime] = FieldInfo(alias="CreationDate", default=None)

    name: Optional[str] = FieldInfo(alias="Name", default=None)


class ListBucketsResponse(BaseModel):
    buckets: Optional[List[Bucket]] = FieldInfo(alias="Buckets", default=None)
