# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CallCreateParams"]


class CallCreateParams(TypedDict, total=False):
    from_: Required[Annotated[str, PropertyInfo(alias="From")]]
    """The E.164-formatted phone number or SIP URI to present as the caller."""

    to: Required[Annotated[str, PropertyInfo(alias="To")]]
    """The E.164-formatted phone number or SIP URI to call."""

    method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="Method")]
    """HTTP method used to retrieve TeXML instructions from Url."""

    texml: Annotated[str, PropertyInfo(alias="Texml")]
    """Inline TeXML instructions to execute when the call is answered."""

    url: Annotated[str, PropertyInfo(alias="Url")]
    """The URL from which to retrieve TeXML instructions.

    Overrides the TeXML application XML request URL.
    """
