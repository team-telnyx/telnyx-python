# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["S3ConfigurationData"]


class S3ConfigurationData(BaseModel):
    aws_access_key_id: Optional[str] = None
    """AWS credentials access key id."""

    aws_secret_access_key: Optional[str] = None
    """AWS secret access key."""

    bucket: Optional[str] = None
    """Name of the bucket to be used to store recording files."""

    region: Optional[str] = None
    """Region where the bucket is located."""
