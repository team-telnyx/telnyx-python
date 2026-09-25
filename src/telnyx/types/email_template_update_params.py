# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["EmailTemplateUpdateParams", "VariableSchema"]


class EmailTemplateUpdateParams(TypedDict, total=False):
    autoescape: bool
    """Per-template HTML autoescaping setting."""

    html_body: Optional[str]
    """Liquid template HTML body."""

    name: str

    strict_variables: bool
    """Per-template strict variable-validation setting."""

    subject: Optional[str]
    """Liquid template subject."""

    text_body: Optional[str]
    """Liquid template text body."""

    variable_schema: Optional[Dict[str, VariableSchema]]
    """Structured variable requirements.

    Required variables cannot define defaults; invalid combinations return 422. Set
    to `null` to clear the schema.
    """

    variables: SequenceNotStr[str]


class VariableSchema(TypedDict, total=False):
    required: Required[bool]
    """
    Whether the variable must be supplied when strict variable validation is
    enabled.
    """

    default: str
    """Default value for an optional variable. Rejected when `required` is `true`."""
