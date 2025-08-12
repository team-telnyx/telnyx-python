# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["CallForwardingParam"]


class CallForwardingParam(TypedDict, total=False):
    call_forwarding_enabled: bool
    """
    Indicates if call forwarding will be enabled for this number if forwards_to and
    forwarding_type are filled in. Defaults to true for backwards compatibility with
    APIV1 use of numbers endpoints.
    """

    forwarding_type: Literal["always", "on-failure"]
    """Call forwarding type. 'forwards_to' must be set for this to have an effect."""

    forwards_to: str
    """The phone number to which inbound calls to this number are forwarded.

    Inbound calls will not be forwarded if this field is left blank. If set, must be
    a +E.164-formatted phone number.
    """
