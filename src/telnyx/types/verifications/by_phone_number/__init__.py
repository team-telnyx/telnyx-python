# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .action_verify_params import ActionVerifyParams as ActionVerifyParams

if TYPE_CHECKING:
    from .verify_verification_code_response import VerifyVerificationCodeResponse as VerifyVerificationCodeResponse


def __getattr__(name: str) -> Any:
    if name == "VerifyVerificationCodeResponse":
        from .verify_verification_code_response import VerifyVerificationCodeResponse

        return VerifyVerificationCodeResponse
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
