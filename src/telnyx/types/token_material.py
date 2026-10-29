# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["TokenMaterial"]


class TokenMaterial(BaseModel):
    """
    What a server needs to mint login tokens for the credential itself, with no request per token (`TelephonyCredential#to_jwt` in telnyx-ruby 3.1.0 or later). As sensitive as `sip_password`: keep it on the server.
    """

    kid: Optional[str] = None
    """Identifies the Telnyx signing key the `signing_secret` was derived with.

    Goes in the token header.
    """

    signing_secret: Optional[str] = None
    """The HMAC-SHA256 key the token is signed with, base64url without padding."""

    tel_token: Optional[str] = None
    """Opaque value Telnyx uses to resolve the credential.

    Carried in the token's `tel_token` claim as is.
    """
