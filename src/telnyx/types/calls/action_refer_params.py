# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ..sip_header_param import SipHeaderParam
from ..custom_sip_header_param import CustomSipHeaderParam

__all__ = ["ActionReferParams"]


class ActionReferParams(TypedDict, total=False):
    sip_address: Required[str]
    """The SIP URI to which the call will be referred to."""

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid execution of duplicate commands.

    Telnyx will ignore subsequent commands with the same `command_id` as one that
    has already been executed.
    """

    custom_headers: Iterable[CustomSipHeaderParam]
    """Custom headers to be added to the SIP INVITE."""

    sip_auth_password: str
    """SIP Authentication password used for SIP challenges."""

    sip_auth_username: str
    """SIP Authentication username used for SIP challenges."""

    sip_headers: Iterable[SipHeaderParam]
    """SIP headers to be added to the request.

    Currently only User-to-User header is supported.
    """
