# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["UacInternalSettingsParam"]


class UacInternalSettingsParam(TypedDict, total=False):
    """Internal Telnyx-side settings for a UAC connection."""

    destination_uri: str
    """
    The SIP URI that Telnyx will call when handling an inbound request from the
    external peer. Do not include a `sip:` prefix. The value must be in the format
    `userinfo@<subdomain.>sip.telnyx.com` or
    `userinfo@<subdomain.>sipdev.telnyx.com`; the userinfo portion may contain only
    letters, digits, hyphens, and underscores.
    """
