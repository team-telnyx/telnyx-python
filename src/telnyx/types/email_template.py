# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EmailTemplate", "VariableSchema"]


class VariableSchema(BaseModel):
    required: bool
    """
    Whether the variable must be supplied when strict variable validation is
    enabled.
    """

    default: Optional[str] = None
    """Default value for an optional variable. Rejected when `required` is `true`."""


class EmailTemplate(BaseModel):
    id: str

    autoescape: bool
    """Whether HTML autoescaping is enabled for this template.

    When `true`, only rendered `html_body` expression output is HTML-escaped at the
    output boundary; `subject` and `text_body` are never autoescaped.
    """

    created_at: datetime

    html_body: Optional[str] = None

    name: str

    record_type: Literal["email_template"]

    strict_variables: bool
    """Whether strict variable validation is enabled for this template.

    When `true`, sends and renders that are missing a variable marked
    `required: true` in `variable_schema` fail with 422 naming the variable.
    """

    subject: Optional[str] = None

    text_body: Optional[str] = None

    updated_at: datetime

    variable_schema: Optional[Dict[str, VariableSchema]] = None
    """
    Structured variable requirements, or `null` when the template uses only the
    legacy `variables` array.
    """

    variables: List[str]
    """Legacy unstructured variable names. This path remains supported unchanged."""
