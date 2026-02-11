# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["MissionCreateParams"]


class MissionCreateParams(TypedDict, total=False):
    name: Required[str]

    description: str

    execution_mode: Literal["external", "managed"]

    instructions: str

    metadata: Dict[str, object]

    model: str
