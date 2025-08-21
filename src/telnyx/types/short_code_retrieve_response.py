# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.short_code import ShortCode

__all__ = ["ShortCodeRetrieveResponse"]


class ShortCodeRetrieveResponse(BaseModel):
    data: Optional[ShortCode] = None
