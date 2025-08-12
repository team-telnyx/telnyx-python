# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MediaUpdateParams"]


class MediaUpdateParams(TypedDict, total=False):
    media_url: str
    """The URL where the media to be stored in Telnyx network is currently hosted.

    The maximum allowed size is 20 MB.
    """

    ttl_secs: int
    """
    The number of seconds after which the media resource will be deleted, defaults
    to 2 days. The maximum allowed vale is 630720000, which translates to 20 years.
    """
