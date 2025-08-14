# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MigrationSourceCreateParams", "ProviderAuth"]


class MigrationSourceCreateParams(TypedDict, total=False):
    bucket_name: Required[str]
    """Bucket name to migrate the data from."""

    provider: Required[Literal["aws", "telnyx"]]
    """Cloud provider from which to migrate data.

    Use 'telnyx' if you want to migrate data from one Telnyx bucket to another.
    """

    provider_auth: Required[ProviderAuth]

    source_region: str
    """
    For intra-Telnyx buckets migration, specify the source bucket region in this
    field.
    """


class ProviderAuth(TypedDict, total=False):
    access_key: str
    """AWS Access Key. For Telnyx-to-Telnyx migrations, use your Telnyx API key here."""

    secret_access_key: str
    """AWS Secret Access Key.

    For Telnyx-to-Telnyx migrations, use your Telnyx API key here as well.
    """
