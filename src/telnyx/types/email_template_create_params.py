# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EmailTemplateCreateParams", "VariableSchema"]


class EmailTemplateCreateParams(TypedDict, total=False):
    name: Required[str]
    """Letters, numbers, spaces, hyphens, and underscores only."""

    autoescape: bool
    """Per-template HTML autoescaping setting.

    Defaults to `false` for backward compatibility. When `true`, the rendered
    `html_body` HTML-escapes each Liquid expression's output at the output boundary
    (after its filters run, before concatenation with literal template markup).
    Input values are never mutated and `subject`/`text_body` are never autoescaped.
    The boundary escape is idempotent: HTML entities already present in the output
    (e.g. from an explicit `escape` filter) are preserved, so an explicit
    `escape`/`escape_once` is never double-escaped, and markup introduced by any
    later filter in the chain is still escaped.
    """

    html_body: Optional[str]
    """Liquid template HTML body."""

    strict_variables: bool
    """Per-template strict variable-validation setting.

    Defaults to `false` for backward compatibility. When `true`, a send or render
    that is missing a variable marked `required: true` in `variable_schema` fails
    with 422 naming the variable. Missing optional variables never fail; their
    schema `default` (when set) is applied to the render.
    """

    subject: Optional[str]
    """Liquid template subject."""

    text_body: Optional[str]
    """Liquid template text body."""

    variable_schema: Optional[Dict[str, VariableSchema]]
    """Structured variable requirements.

    Required variables cannot define defaults; invalid combinations return 422. This
    is independent of the legacy `variables` array. On render with
    `strict_variables` enabled: `required` variables must be supplied as non-empty
    values — absent, `null`, empty string, empty object `{}`, and empty array `[]`
    all fail with 422 naming the variable, while present values such as `false` and
    `0` pass (they are present, not empty). Optional variables fall back to their
    `default` when absent.
    """

    variables: SequenceNotStr[str]
    """Template variables. Auto-extracted from subject/body fields when absent."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]


class VariableSchema(TypedDict, total=False):
    required: Required[bool]
    """
    Whether the variable must be supplied when strict variable validation is
    enabled.
    """

    default: str
    """Default value for an optional variable. Rejected when `required` is `true`."""
