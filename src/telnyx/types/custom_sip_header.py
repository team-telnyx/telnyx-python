# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["CustomSipHeader"]


class CustomSipHeader(BaseModel):
    name: str
    """The name of the header to add."""

    value: str
    """The value of the header."""
