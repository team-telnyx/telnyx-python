# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "CustomStorageCredentialRetrieveResponse",
    "Data",
    "DataConfiguration",
    "DataConfigurationGcsConfigurationData",
    "DataConfigurationS3ConfigurationData",
    "DataConfigurationAzureConfigurationData",
]


class DataConfigurationGcsConfigurationData(BaseModel):
    bucket: Optional[str] = None
    """Name of the bucket to be used to store recording files."""

    credentials: Optional[str] = None
    """
    Opaque credential token used to authenticate and authorize with storage
    provider.
    """


class DataConfigurationS3ConfigurationData(BaseModel):
    aws_access_key_id: Optional[str] = None
    """AWS credentials access key id."""

    aws_secret_access_key: Optional[str] = None
    """AWS secret access key."""

    bucket: Optional[str] = None
    """Name of the bucket to be used to store recording files."""

    region: Optional[str] = None
    """Region where the bucket is located."""


class DataConfigurationAzureConfigurationData(BaseModel):
    account_key: Optional[str] = None
    """Azure Blob Storage account key."""

    account_name: Optional[str] = None
    """Azure Blob Storage account name."""

    bucket: Optional[str] = None
    """Name of the bucket to be used to store recording files."""


DataConfiguration: TypeAlias = Union[
    DataConfigurationGcsConfigurationData, DataConfigurationS3ConfigurationData, DataConfigurationAzureConfigurationData
]


class Data(BaseModel):
    backend: Literal["gcs", "s3", "azure"]

    configuration: DataConfiguration


class CustomStorageCredentialRetrieveResponse(BaseModel):
    connection_id: str
    """
    Uniquely identifies a Telnyx application (Call Control, TeXML) or Sip connection
    resource.
    """

    data: Data

    record_type: Literal["custom_storage_credentials"]
    """Identifies record type."""
