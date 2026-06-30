# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .rc_send_params import RcSendParams as RcSendParams
from .rc_generate_deeplink_params import RcGenerateDeeplinkParams as RcGenerateDeeplinkParams

if TYPE_CHECKING:
    from .rc_send_response import RcSendResponse as RcSendResponse
    from .rc_generate_deeplink_response import RcGenerateDeeplinkResponse as RcGenerateDeeplinkResponse


def __getattr__(name: str) -> Any:
    if name == "RcGenerateDeeplinkResponse":
        from .rc_generate_deeplink_response import RcGenerateDeeplinkResponse

        return RcGenerateDeeplinkResponse
    if name == "RcSendResponse":
        from .rc_send_response import RcSendResponse

        return RcSendResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
