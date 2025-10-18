# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["JobError", "Meta", "Source"]


class Meta(BaseModel):
    url: Optional[str] = None
    """URL with additional information on the error."""


class Source(BaseModel):
    parameter: Optional[str] = None
    """Indicates which query parameter caused the error."""

    pointer: Optional[str] = None
    """JSON pointer (RFC6901) to the offending entity."""


class JobError(BaseModel):
    code: str

    title: str

    detail: Optional[str] = None

    meta: Optional[Meta] = None

    source: Optional[Source] = None
