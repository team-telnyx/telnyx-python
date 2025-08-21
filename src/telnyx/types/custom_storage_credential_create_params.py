# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .s3_configuration_data_param import S3ConfigurationDataParam
from .gcs_configuration_data_param import GcsConfigurationDataParam
from .azure_configuration_data_param import AzureConfigurationDataParam

__all__ = ["CustomStorageCredentialCreateParams", "Configuration"]


class CustomStorageCredentialCreateParams(TypedDict, total=False):
    backend: Required[Literal["gcs", "s3", "azure"]]

    configuration: Required[Configuration]


Configuration: TypeAlias = Union[GcsConfigurationDataParam, S3ConfigurationDataParam, AzureConfigurationDataParam]
