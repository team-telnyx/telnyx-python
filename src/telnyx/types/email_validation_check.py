# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EmailValidationCheck"]


class EmailValidationCheck(BaseModel):
    pass_: bool = FieldInfo(alias="pass")

    details: Optional[str] = None
    """Human-readable check detail. Omitted when nil."""
