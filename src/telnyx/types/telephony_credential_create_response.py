# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .telephony_credential import TelephonyCredential

__all__ = ["TelephonyCredentialCreateResponse"]


class TelephonyCredentialCreateResponse(BaseModel):
    data: Optional[TelephonyCredential] = None
