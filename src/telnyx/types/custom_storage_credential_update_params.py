# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .s3_configuration_data_param import S3ConfigurationDataParam
from .gcs_configuration_data_param import GcsConfigurationDataParam
from .azure_configuration_data_param import AzureConfigurationDataParam
from .s3_generic_configuration_data_param import S3GenericConfigurationDataParam

__all__ = ["CustomStorageCredentialUpdateParams", "Configuration"]


class CustomStorageCredentialUpdateParams(TypedDict, total=False):
    backend: Required[Literal["gcs", "s3", "s3-generic", "azure"]]

    configuration: Required[Configuration]


Configuration: TypeAlias = Union[
    GcsConfigurationDataParam, S3ConfigurationDataParam, S3GenericConfigurationDataParam, AzureConfigurationDataParam
]
