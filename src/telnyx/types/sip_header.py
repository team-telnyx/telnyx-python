# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SipHeader"]


class SipHeader(BaseModel):
    name: Literal["User-to-User"]
    """The name of the header to add."""

    value: str
    """The value of the header."""
