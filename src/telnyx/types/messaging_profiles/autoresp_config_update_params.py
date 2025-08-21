# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AutorespConfigUpdateParams"]


class AutorespConfigUpdateParams(TypedDict, total=False):
    profile_id: Required[str]

    country_code: Required[str]

    keywords: Required[List[str]]

    op: Required[Literal["start", "stop", "info"]]

    resp_text: str
