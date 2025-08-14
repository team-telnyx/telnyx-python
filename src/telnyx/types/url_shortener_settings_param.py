# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["URLShortenerSettingsParam"]


class URLShortenerSettingsParam(TypedDict, total=False):
    domain: Required[str]
    """One of the domains provided by the Telnyx URL shortener service."""

    prefix: str
    """
    Optional prefix that can be used to identify your brand, and will appear in the
    Telnyx generated URLs after the domain name.
    """

    replace_blacklist_only: bool
    """
    Use the link replacement tool only for links that are specifically blacklisted
    by Telnyx.
    """

    send_webhooks: bool
    """Receive webhooks for when your replaced links are clicked.

    Webhooks are sent to the webhooks on the messaging profile.
    """
