# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["UacInternalSettings"]


class UacInternalSettings(BaseModel):
    """Internal Telnyx-side settings for a UAC connection."""

    destination_uri: Optional[str] = None
    """
    The SIP URI that Telnyx will call when handling an inbound request from the
    external peer. Do not include a `sip:` prefix. The value must be in the format
    `userinfo@<subdomain.>sip.telnyx.com` or
    `userinfo@<subdomain.>sipdev.telnyx.com`; the userinfo portion may contain only
    letters, digits, hyphens, and underscores.
    """
