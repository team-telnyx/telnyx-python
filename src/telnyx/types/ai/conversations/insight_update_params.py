# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

__all__ = ["InsightUpdateParams"]


class InsightUpdateParams(TypedDict, total=False):
    instructions: str

    json_schema: Union[str, object]

    name: str

    webhook: str
