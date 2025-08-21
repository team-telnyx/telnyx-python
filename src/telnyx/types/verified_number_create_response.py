# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VerifiedNumberCreateResponse"]


class VerifiedNumberCreateResponse(BaseModel):
    phone_number: Optional[str] = None

    verification_method: Optional[str] = None
