# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MediaUploadParams"]


class MediaUploadParams(TypedDict, total=False):
    media_url: Required[str]
    """The URL where the media to be stored in Telnyx network is currently hosted.

    The maximum allowed size is 20 MB.
    """

    media_name: str
    """The unique identifier of a file."""

    ttl_secs: int
    """
    The number of seconds after which the media resource will be deleted, defaults
    to 2 days. The maximum allowed vale is 630720000, which translates to 20 years.
    """
