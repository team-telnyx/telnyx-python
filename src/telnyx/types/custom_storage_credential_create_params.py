# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, ForwardRef
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["CustomStorageCredentialCreateParams", "Configuration"]


class CustomStorageCredentialCreateParams(TypedDict, total=False):
    backend: Required[Literal["gcs", "s3", "s3-generic", "azure"]]

    configuration: Required[Configuration]


if TYPE_CHECKING:
    Configuration: TypeAlias = Union[
        "GcsConfigurationDataParam",
        "S3ConfigurationDataParam",
        "S3GenericConfigurationDataParam",
        "AzureConfigurationDataParam",
    ]
else:
    Configuration = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).GcsConfigurationDataParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).S3ConfigurationDataParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).S3GenericConfigurationDataParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AzureConfigurationDataParam"),
    ]

from .s3_configuration_data_param import S3ConfigurationDataParam
from .gcs_configuration_data_param import GcsConfigurationDataParam
from .azure_configuration_data_param import AzureConfigurationDataParam
from .s3_generic_configuration_data_param import S3GenericConfigurationDataParam
