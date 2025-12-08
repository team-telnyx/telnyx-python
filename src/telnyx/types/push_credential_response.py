# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .push_credential import PushCredential

__all__ = ["PushCredentialResponse"]


class PushCredentialResponse(BaseModel):
    """Success response with details about a push credential"""

    data: Optional[PushCredential] = None
