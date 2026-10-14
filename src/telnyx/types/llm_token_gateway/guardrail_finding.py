# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GuardrailFinding"]


class GuardrailFinding(BaseModel):
    action: Literal["flag", "block"]

    code: str

    count: int

    detector: Literal["secrets", "dlp", "safety"]
