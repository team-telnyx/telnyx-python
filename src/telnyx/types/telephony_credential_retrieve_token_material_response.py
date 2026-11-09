# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel
from .token_material import TokenMaterial

__all__ = ["TelephonyCredentialRetrieveTokenMaterialResponse"]


class TelephonyCredentialRetrieveTokenMaterialResponse(BaseModel):
    data: Optional[TokenMaterial] = None
    """
    What a server needs to mint login tokens for the credential itself, with no
    request per token (`TelephonyCredential#to_jwt` in telnyx-ruby 3.1.0 or later).
    As sensitive as `sip_password`: keep it on the server.
    """
