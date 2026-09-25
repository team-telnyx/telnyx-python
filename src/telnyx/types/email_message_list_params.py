# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EmailMessageListParams"]


class EmailMessageListParams(TypedDict, total=False):
    filter_metadata: Annotated[str, PropertyInfo(alias="filter[metadata]")]
    """
    Metadata containment filter, supplied as a JSON object or comma-separated
    `key=value` pairs. All supplied key/value pairs must be contained in the message
    metadata. An empty value or empty JSON object omits the filter. Malformed
    values, valid non-object JSON, pairs without `=`, empty keys, and
    non-string/nested query shapes return HTTP 400.
    """

    filter_tags: Annotated[str, PropertyInfo(alias="filter[tags]")]
    """Comma-separated tags.

    Each segment is trimmed, and messages having at least one supplied tag are
    returned; matching is exact and case-sensitive after trimming. Because commas
    delimit values and surrounding whitespace is removed, this filter cannot
    represent stored tags containing literal commas or leading/trailing whitespace.
    An empty value omits the filter. Empty segments and non-string/nested query
    shapes return HTTP 400.
    """

    page_cursor: str
    """Opaque URL-safe Base64 cursor returned by a previous list response."""

    page_size: int
    """Number of results to return.

    Defaults to 25; maximum is 100. Invalid values are clamped to the valid range.
    """
