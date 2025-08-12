# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MigrationCreateParams"]


class MigrationCreateParams(TypedDict, total=False):
    source_id: Required[str]
    """ID of the Migration Source from which to migrate data."""

    target_bucket_name: Required[str]
    """Bucket name to migrate the data into.

    Will default to the same name as the `source_bucket_name`.
    """

    target_region: Required[str]
    """Telnyx Cloud Storage region to migrate the data to."""

    refresh: bool
    """
    If true, will continue to poll the source bucket to ensure new data is
    continually migrated over.
    """
