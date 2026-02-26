# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WhatsappLocation"]


class WhatsappLocation(BaseModel):
    address: Optional[str] = None

    latitude: Optional[str] = None

    longitude: Optional[str] = None

    name: Optional[str] = None
