# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["PhotoRetrieveResponse", "Data"]


class Data(BaseModel):
    phone_number_id: Optional[str] = None
    """Meta phone number ID"""

    profile_photo_url: Optional[str] = None
    """URL of the business profile photo (served by Meta's CDN).

    May be empty if no photo is set.
    """

    record_type: Optional[str] = None


class PhotoRetrieveResponse(BaseModel):
    data: Optional[Data] = None
