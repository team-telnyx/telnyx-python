# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ExternalConnectionUpdateLocationResponse", "Data"]


class Data(BaseModel):
    accepted_address_suggestions: Optional[bool] = None

    location_id: Optional[str] = None

    static_emergency_address_id: Optional[str] = None


class ExternalConnectionUpdateLocationResponse(BaseModel):
    data: Optional[Data] = None
