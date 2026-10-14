# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailTemplateListParams"]


class EmailTemplateListParams(TypedDict, total=False):
    filter_autoescape: Annotated[Literal["true", "false"], PropertyInfo(alias="filter[autoescape]")]
    """Exact match on the template's `autoescape` option.

    Only the exact query strings `true` and `false` are accepted; other values,
    including blank, return 400.
    """

    filter_content_type: Annotated[
        Literal["html_and_text", "html_only", "text_only", "no_body"], PropertyInfo(alias="filter[content_type]")
    ]
    """Matches templates by stored body presence.

    `html_and_text` requires both an HTML and text body; `html_only` requires HTML
    and no text body; `text_only` requires text and no HTML body; `no_body` requires
    neither. `null` and exactly `""` count as absent; whitespace-only strings count
    as content. An empty or unsupported value returns a 400 response.
    """

    filter_query: Annotated[str, PropertyInfo(alias="filter[query]")]
    """
    Case-insensitive literal substring match over the template `name` or stored
    `subject` only; bodies are never searched. `%`, `_`, and `\\`` are literal
    characters with no wildcard meaning. A blank value is treated as omitted.
    """

    filter_strict_variables: Annotated[Literal["true", "false"], PropertyInfo(alias="filter[strict_variables]")]
    """Exact match on the template's `strict_variables` option.

    Only the exact query strings `true` and `false` are accepted; other values,
    including blank, return 400.
    """

    page_cursor: str
    """Opaque URL-safe Base64 cursor returned by a previous list response."""

    page_size: int
    """Number of results to return.

    Defaults to 25; maximum is 100. Invalid values are clamped to the valid range.
    """
