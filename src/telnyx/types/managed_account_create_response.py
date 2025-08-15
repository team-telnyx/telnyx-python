# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .managed_account import ManagedAccount

__all__ = ["ManagedAccountCreateResponse"]


class ManagedAccountCreateResponse(BaseModel):
    data: Optional[ManagedAccount] = None
