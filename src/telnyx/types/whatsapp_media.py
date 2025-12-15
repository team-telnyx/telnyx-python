# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["WhatsappMedia"]


class WhatsappMedia(BaseModel):
    caption: Optional[str] = None
    """media caption"""

    filename: Optional[str] = None
    """file name with extension"""

    link: Optional[str] = None
    """media URL"""

    voice: Optional[bool] = None
    """true if voice message"""
