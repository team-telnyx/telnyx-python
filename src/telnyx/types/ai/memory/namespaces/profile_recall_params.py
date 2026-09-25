# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ProfileRecallParams"]


class ProfileRecallParams(TypedDict, total=False):
    namespace: Required[str]

    query: Required[str]

    top_k: Optional[int]
