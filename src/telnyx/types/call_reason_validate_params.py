# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["CallReasonValidateParams"]


class CallReasonValidateParams(TypedDict, total=False):
    body: Required[SequenceNotStr[str]]
    """
    **Bare JSON array** of candidate call-reason strings (NOT an object - there is
    no top-level `call_reasons` key on this endpoint). 1–10 strings, each ≤64
    characters.
    """
