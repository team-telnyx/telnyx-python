# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .source_type import SourceType

__all__ = ["SourceRequestParam"]


class SourceRequestParam(TypedDict, total=False):
    source_type: Required[SourceType]
    """The type of Telnyx data attached as a source.

    `bucket` requires an additional `bucket_id`. Only `voice` is searchable today;
    `meeting_bot`, `message`, and `bucket` attach but are not yet searchable (Coming
    soon).
    """

    bucket_id: str
    """The Telnyx Storage bucket name.

    Required when `source_type` is `bucket`; ignored otherwise.
    """
