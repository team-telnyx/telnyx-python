# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["EmailTemplateUpdateParams"]


class EmailTemplateUpdateParams(TypedDict, total=False):
    html_body: Optional[str]
    """Liquid template HTML body."""

    name: str

    subject: Optional[str]
    """Liquid template subject."""

    text_body: Optional[str]
    """Liquid template text body."""

    variables: SequenceNotStr[str]
