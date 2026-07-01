# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_verify_params import ActionVerifyParams as ActionVerifyParams

if TYPE_CHECKING:
    from .verify_meta import VerifyMeta as VerifyMeta
    from .by_phone_number_list_response import ByPhoneNumberListResponse as ByPhoneNumberListResponse


def __getattr__(name: str) -> Any:
    if name == "VerifyMeta":
        from .verify_meta import VerifyMeta

        return VerifyMeta
    if name == "ByPhoneNumberListResponse":
        from .by_phone_number_list_response import ByPhoneNumberListResponse

        return ByPhoneNumberListResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
