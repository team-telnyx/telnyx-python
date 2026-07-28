# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .s3_configuration_data import S3ConfigurationData
from .gcs_configuration_data import GcsConfigurationData
from .azure_configuration_data import AzureConfigurationData

__all__ = ["CustomStorageConfiguration", "Configuration", "ConfigurationS3GenericConfigurationData"]


class ConfigurationS3GenericConfigurationData(BaseModel):
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


Configuration: TypeAlias = Annotated[
    Union[GcsConfigurationData, S3ConfigurationData, ConfigurationS3GenericConfigurationData, AzureConfigurationData],
    PropertyInfo(discriminator="backend"),
]


class CustomStorageConfiguration(BaseModel):
    backend: Literal["gcs", "s3", "s3-generic", "azure"]

    configuration: Configuration
