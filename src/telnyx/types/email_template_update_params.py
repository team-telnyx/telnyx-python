# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

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

    variables: Optional[SequenceNotStr[str]]
    """Persisted variable names.

    In `automatic` mode a non-null array is rejected; in `explicit` mode this is the
    exact manual array and each item is limited to 255 Unicode code points.
    """

    variables_mode: Literal["automatic", "explicit"]
    """Controls how `variables` is maintained.

    Setting `automatic` re-extracts immediately from the effective subject, HTML
    body, and text body and rejects a simultaneous non-null array. Setting
    `explicit` requires the exact non-null array, including valid `[]`. With the
    mode omitted, a non-null array selects explicit mode, null selects automatic
    mode, and omitting both fields preserves the current mode. Source-content
    changes re-extract only in automatic mode.
    """


class VariableSchema(TypedDict, total=False):
    required: Required[bool]
    """
    Whether the variable must be supplied when strict variable validation is
    enabled.
    """

    default: str
    """Default value for an optional variable. Rejected when `required` is `true`."""
