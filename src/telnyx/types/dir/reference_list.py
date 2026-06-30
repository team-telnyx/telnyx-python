# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .reference import Reference

__all__ = ["ReferenceList"]


class ReferenceList(BaseModel):
    data: List[Reference]
