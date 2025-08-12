# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CallForwarding"]


class CallForwarding(BaseModel):
    call_forwarding_enabled: Optional[bool] = None
    """
    Indicates if call forwarding will be enabled for this number if forwards_to and
    forwarding_type are filled in. Defaults to true for backwards compatibility with
    APIV1 use of numbers endpoints.
    """

    forwarding_type: Optional[Literal["always", "on-failure"]] = None
    """Call forwarding type. 'forwards_to' must be set for this to have an effect."""

    forwards_to: Optional[str] = None
    """The phone number to which inbound calls to this number are forwarded.

    Inbound calls will not be forwarded if this field is left blank. If set, must be
    a +E.164-formatted phone number.
    """
