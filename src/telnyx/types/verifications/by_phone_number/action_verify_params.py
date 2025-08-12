# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionVerifyParams"]


class ActionVerifyParams(TypedDict, total=False):
    code: Required[str]
    """This is the code the user submits for verification."""

    verify_profile_id: Required[str]
    """The identifier of the associated Verify profile."""
