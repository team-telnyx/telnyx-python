# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .credential_connection import CredentialConnection

__all__ = ["CredentialConnectionCreateResponse"]


class CredentialConnectionCreateResponse(BaseModel):
    data: Optional[CredentialConnection] = None
