# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .s3_configuration_data import S3ConfigurationData
from .gcs_configuration_data import GcsConfigurationData
from .azure_configuration_data import AzureConfigurationData

__all__ = ["CustomStorageConfiguration", "Configuration"]

Configuration: TypeAlias = Annotated[
    Union[GcsConfigurationData, S3ConfigurationData, AzureConfigurationData], PropertyInfo(discriminator="backend")
]


class CustomStorageConfiguration(BaseModel):
    backend: Literal["gcs", "s3", "azure"]

    configuration: Configuration
