# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["JobDeleteBatchParams"]


class JobDeleteBatchParams(TypedDict, total=False):
    phone_numbers: Required[List[str]]
