# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InboundSipHeader"]


class InboundSipHeader(BaseModel):
    name: Literal["User-to-User", "Diversion"]
    """The name of the header received from the SIP INVITE."""

    value: str
    """The value of the header."""
