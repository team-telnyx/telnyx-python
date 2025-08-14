# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "CustomStorageCredentialCreateParams",
    "Configuration",
    "ConfigurationGcsConfigurationData",
    "ConfigurationS3ConfigurationData",
    "ConfigurationAzureConfigurationData",
]


class CustomStorageCredentialCreateParams(TypedDict, total=False):
    backend: Required[Literal["gcs", "s3", "azure"]]

    configuration: Required[Configuration]


class ConfigurationGcsConfigurationData(TypedDict, total=False):
    bucket: str
    """Name of the bucket to be used to store recording files."""

    credentials: str
    """
    Opaque credential token used to authenticate and authorize with storage
    provider.
    """


class ConfigurationS3ConfigurationData(TypedDict, total=False):
    aws_access_key_id: str
    """AWS credentials access key id."""

    aws_secret_access_key: str
    """AWS secret access key."""

    bucket: str
    """Name of the bucket to be used to store recording files."""

    region: str
    """Region where the bucket is located."""


class ConfigurationAzureConfigurationData(TypedDict, total=False):
    account_key: str
    """Azure Blob Storage account key."""

    account_name: str
    """Azure Blob Storage account name."""

    bucket: str
    """Name of the bucket to be used to store recording files."""


Configuration: TypeAlias = Union[
    ConfigurationGcsConfigurationData, ConfigurationS3ConfigurationData, ConfigurationAzureConfigurationData
]
