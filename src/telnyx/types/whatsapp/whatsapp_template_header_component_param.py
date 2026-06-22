# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["WhatsappTemplateHeaderComponentParam", "Example"]


class Example(TypedDict, total=False):
    """Sample values for header variables."""

    header_handle: SequenceNotStr[str]
    """Media handle for IMAGE, VIDEO, or DOCUMENT headers."""

    header_text: SequenceNotStr[str]
    """Sample values for text header variables."""


class WhatsappTemplateHeaderComponentParam(TypedDict, total=False):
    """Optional header displayed at the top of the message."""

    format: Required[Literal["TEXT", "IMAGE", "VIDEO", "DOCUMENT", "LOCATION"]]
    """
    Header format type: TEXT (supports one variable), IMAGE, VIDEO, DOCUMENT, or
    LOCATION.
    """

    type: Required[Literal["HEADER"]]

    example: Example
    """Sample values for header variables."""

    text: str
    """Header text.

    Required when format is TEXT. Supports one variable ({{1}}). Variables cannot be
    at the start or end.
    """
