# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailTemplateCreateParams"]


class EmailTemplateCreateParams(TypedDict, total=False):
    name: Required[str]
    """Letters, numbers, spaces, hyphens, and underscores only."""

    html_body: Optional[str]
    """Liquid template HTML body."""

    subject: Optional[str]
    """Liquid template subject."""

    text_body: Optional[str]
    """Liquid template text body."""

    variables: SequenceNotStr[str]
    """Template variables. Auto-extracted from subject/body fields when absent."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
