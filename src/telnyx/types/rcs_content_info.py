# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["RcsContentInfo"]


class RcsContentInfo(BaseModel):
    file_url: str
    """Publicly reachable URL of the file."""

    force_refresh: Optional[bool] = None
    """If set the URL content will not be cached."""

    thumbnail_url: Optional[str] = None
    """Publicly reachable URL of the thumbnail. Maximum size of 100 kB."""
