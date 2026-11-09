# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VariableSchemaEntryParam"]


class VariableSchemaEntryParam(TypedDict, total=False):
    required: Required[bool]
    """
    Whether the variable must be supplied when strict variable validation is
    enabled.
    """

    default: str
    """Default value for an optional variable. Rejected when `required` is `true`."""
