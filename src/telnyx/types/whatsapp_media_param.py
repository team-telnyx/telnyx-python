# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["WhatsappMediaParam"]


class WhatsappMediaParam(TypedDict, total=False):
    caption: str
    """media caption"""

    filename: str
    """file name with extension"""

    link: str
    """media URL"""

    voice: bool
    """true if voice message"""
