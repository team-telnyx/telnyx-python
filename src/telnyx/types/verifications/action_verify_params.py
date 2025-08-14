# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ActionVerifyParams"]


class ActionVerifyParams(TypedDict, total=False):
    code: str
    """This is the code the user submits for verification."""

    status: Literal["accepted", "rejected"]
    """Identifies if the verification code has been accepted or rejected.

    Only permitted if custom_code was used for the verification.
    """
