# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["VoicemailRetrieveResponse", "Data"]


class Data(BaseModel):
    enabled: Optional[bool] = None
    """Whether voicemail is enabled."""

    pin: Optional[str] = None
    """The pin used for the voicemail."""


class VoicemailRetrieveResponse(BaseModel):
    data: Optional[Data] = None
