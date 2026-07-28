# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["S3ConfigurationData"]


class S3ConfigurationData(BaseModel):
    aws_access_key_id: str
    """AWS credentials access key id."""

    aws_secret_access_key: str
    """AWS secret access key."""

    backend: Literal["s3"]
    """Storage backend type"""

    bucket: str
    """Name of the bucket to be used to store recording files."""

    region: str
    """Region where the bucket is located."""
