# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AutorespConfigUpdateParams"]


class AutorespConfigUpdateParams(TypedDict, total=False):
    profile_id: Required[str]

    country_code: Required[str]

    keywords: Required[SequenceNotStr[str]]

    op: Required[Literal["start", "stop", "info"]]

    resp_text: str
