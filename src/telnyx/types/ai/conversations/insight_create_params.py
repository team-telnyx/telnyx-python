# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Required, TypedDict

__all__ = ["InsightCreateParams"]


class InsightCreateParams(TypedDict, total=False):
    instructions: Required[str]

    name: Required[str]

    json_schema: Union[str, Dict[str, object]]
    """If specified, the output will follow the JSON schema."""

    webhook: str
