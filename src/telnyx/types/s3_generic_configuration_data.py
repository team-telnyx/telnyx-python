# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["S3GenericConfigurationData"]


class S3GenericConfigurationData(BaseModel):
    aws_access_key_id: str
    """AWS credentials access key id."""

    aws_secret_access_key: str
    """AWS secret access key."""

    backend: Literal["s3-generic"]
    """Storage backend type"""

    bucket: str
    """Name of the bucket to be used to store recording files."""

    endpoint: str
    """
    URL of an S3-compatible storage endpoint, used to direct uploads and presigned
    download URLs to a non-AWS store (for example MinIO, Cloudflare R2, Wasabi,
    Backblaze B2, or Supabase). A bare host (https://s3.example.com) or a
    path-prefixed URL (https://xyz.supabase.co/storage/v1/s3) is accepted, and must
    use the http or https scheme.
    """

    region: str
    """Region where the bucket is located."""
