# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AISummarizeParams"]


class AISummarizeParams(TypedDict, total=False):
    bucket: Required[str]
    """The name of the bucket that contains the file to be summarized."""

    filename: Required[str]
    """The name of the file to be summarized."""

    system_prompt: str
    """A system prompt to guide the summary generation."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
