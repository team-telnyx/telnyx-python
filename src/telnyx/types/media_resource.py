# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MediaResource"]


class MediaResource(BaseModel):
    content_type: Optional[str] = None
    """Content type of the file"""

    created_at: Optional[str] = None
    """ISO 8601 formatted date of when the media resource was created"""

    expires_at: Optional[str] = None
    """ISO 8601 formatted date of when the media resource will expire and be deleted."""

    media_name: Optional[str] = None
    """Uniquely identifies a media resource."""

    updated_at: Optional[str] = None
    """ISO 8601 formatted date of when the media resource was last updated"""
