# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["EinBrandIdentifier"]


class EinBrandIdentifier(BaseModel):
    identifier_type: Literal["EIN"]

    value: str
    """Nine digits, optionally formatted as NN-NNNNNNN."""
