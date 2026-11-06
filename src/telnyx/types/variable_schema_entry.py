# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["VariableSchemaEntry"]


class VariableSchemaEntry(BaseModel):
    required: bool
    """
    Whether the variable must be supplied when strict variable validation is
    enabled.
    """

    default: Optional[str] = None
    """Default value for an optional variable. Rejected when `required` is `true`."""
