# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BrandContact"]


class BrandContact(BaseModel):
    contact_type: Literal["BRAND", "PRIMARY", "OFFICER", "AGENT", "RESPONSIBLE_PARTY", "BILLING", "UNKNOWN"]

    email: str

    first_name: str

    last_name: str

    phone_number: str

    title: Optional[str] = None
