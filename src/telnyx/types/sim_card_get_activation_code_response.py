# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SimCardGetActivationCodeResponse", "Data"]


class Data(BaseModel):
    activation_code: Optional[str] = None
    """Contents of the eSIM activation QR code."""

    record_type: Optional[str] = None


class SimCardGetActivationCodeResponse(BaseModel):
    data: Optional[Data] = None
