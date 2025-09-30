# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Error", "Source"]


class Source(BaseModel):
    parameter: Optional[str] = None
    """Indicates which query parameter caused the error."""

    pointer: Optional[str] = None
    """JSON pointer (RFC6901) to the offending entity."""


class Error(BaseModel):
    code: str

    title: str

    detail: Optional[str] = None

    meta: Optional[Dict[str, object]] = None

    source: Optional[Source] = None
