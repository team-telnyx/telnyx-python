# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["URLShortenerSettings"]


class URLShortenerSettings(BaseModel):
    domain: str
    """One of the domains provided by the Telnyx URL shortener service."""

    prefix: Optional[str] = None
    """
    Optional prefix that can be used to identify your brand, and will appear in the
    Telnyx generated URLs after the domain name.
    """

    replace_blacklist_only: Optional[bool] = None
    """
    Use the link replacement tool only for links that are specifically blacklisted
    by Telnyx.
    """

    send_webhooks: Optional[bool] = None
    """Receive webhooks for when your replaced links are clicked.

    Webhooks are sent to the webhooks on the messaging profile.
    """
