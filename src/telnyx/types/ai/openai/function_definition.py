# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["FunctionDefinition"]


class FunctionDefinition(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[Dict[str, object]] = None
