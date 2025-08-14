# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CallUpdateParams"]


class CallUpdateParams(TypedDict, total=False):
    fallback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="FallbackMethod")]
    """HTTP request type used for `FallbackUrl`."""

    fallback_url: Annotated[str, PropertyInfo(alias="FallbackUrl")]
    """
    A failover URL for which Telnyx will retrieve the TeXML call instructions if the
    Url is not responding.
    """

    method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="Method")]
    """HTTP request type used for `Url`."""

    status: Annotated[str, PropertyInfo(alias="Status")]
    """The value to set the call status to.

    Setting the status to completed ends the call.
    """

    status_callback: Annotated[str, PropertyInfo(alias="StatusCallback")]
    """URL destination for Telnyx to send status callback events to for the call."""

    status_callback_method: Annotated[Literal["GET", "POST"], PropertyInfo(alias="StatusCallbackMethod")]
    """HTTP request type used for `StatusCallback`."""

    texml: Annotated[str, PropertyInfo(alias="Texml")]
    """TeXML to replace the current one with."""

    url: Annotated[str, PropertyInfo(alias="Url")]
    """
    The URL where TeXML will make a request to retrieve a new set of TeXML
    instructions to continue the call flow.
    """
