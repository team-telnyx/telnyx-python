# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .s3_configuration_data import S3ConfigurationData
from .gcs_configuration_data import GcsConfigurationData
from .azure_configuration_data import AzureConfigurationData

__all__ = ["CustomStorageConfiguration", "Configuration"]

Configuration: TypeAlias = Union[GcsConfigurationData, S3ConfigurationData, AzureConfigurationData]


class CustomStorageConfiguration(BaseModel):
    backend: Literal["gcs", "s3", "azure"]

    configuration: Configuration
