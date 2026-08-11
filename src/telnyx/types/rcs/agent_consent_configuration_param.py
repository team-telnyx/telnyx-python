# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentConsentConfigurationParam", "OptInMethod"]


class OptInMethod(TypedDict, total=False):
    method_type: Required[Literal["SMS", "WEBSITE", "MOBILE_APP", "QR_CODE", "SALE_POINT", "OTHER"]]

    description: Optional[str]
    """Required when method_type is `OTHER`."""


class AgentConsentConfigurationParam(TypedDict, total=False):
    call_to_action: Required[str]

    double_opt_in: Required[bool]

    help_response: Required[str]

    opt_in_message: Required[str]

    opt_in_methods: Required[Iterable[OptInMethod]]

    opt_out_response: Required[str]

    call_to_action_media_url: Optional[str]
    """Required when an opt-in method is `WEBSITE` or `MOBILE_APP`."""

    call_to_action_url: Optional[str]
    """Required when an opt-in method is `WEBSITE`."""

    double_opt_in_message: Optional[str]
    """Required when double_opt_in is true."""
