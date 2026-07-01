# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .dir.dir import Dir
from .._models import BaseModel

__all__ = ["DirWrapped"]


class DirWrapped(BaseModel):
    data: Dir
