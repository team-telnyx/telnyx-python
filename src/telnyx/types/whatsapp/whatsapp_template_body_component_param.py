# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["WhatsappTemplateBodyComponentParam", "Example"]


class Example(TypedDict, total=False):
    """Sample values for body variables. Required when body text contains parameters."""

    body_text: Iterable[SequenceNotStr[str]]
    """Array containing one array of sample values, one per variable in order."""


class WhatsappTemplateBodyComponentParam(TypedDict, total=False):
    """The main text content of the message.

    Supports multiple variable parameters ({{1}}, {{2}}, etc.). Variables cannot be at the start or end. Maximum 1024 characters.
    """

    type: Required[Literal["BODY"]]

    example: Example
    """Sample values for body variables. Required when body text contains parameters."""

    text: str
    """Body text content.

    Use {{1}}, {{2}}, etc. for variable placeholders. Required for MARKETING and
    UTILITY templates. Optional for AUTHENTICATION templates where Meta provides the
    built-in OTP body.
    """
