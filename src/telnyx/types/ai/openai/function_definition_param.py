# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["FunctionDefinitionParam"]


class FunctionDefinitionParam(TypedDict, total=False):
    name: Required[str]

    description: str

    parameters: Dict[str, object]
