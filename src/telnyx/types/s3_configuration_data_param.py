# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["S3ConfigurationDataParam"]


class S3ConfigurationDataParam(TypedDict, total=False):
    aws_access_key_id: str
    """AWS credentials access key id."""

    aws_secret_access_key: str
    """AWS secret access key."""

    bucket: str
    """Name of the bucket to be used to store recording files."""

    region: str
    """Region where the bucket is located."""
