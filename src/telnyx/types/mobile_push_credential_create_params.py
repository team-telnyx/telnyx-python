# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MobilePushCredentialCreateParams",
    "CreateMobilePushCredentialRequest",
    "CreateMobilePushCredentialRequestIos",
    "CreateMobilePushCredentialRequestAndroid",
]


class MobilePushCredentialCreateParams(TypedDict, total=False):
    create_mobile_push_credential_request: Required[
        Annotated[CreateMobilePushCredentialRequest, PropertyInfo(alias="createMobilePushCredentialRequest")]
    ]


class CreateMobilePushCredentialRequestIos(TypedDict, total=False):
    alias: Required[str]
    """Alias to uniquely identify the credential"""

    certificate: Required[str]
    """Certificate as received from APNs"""

    private_key: Required[str]
    """Corresponding private key to the certificate as received from APNs"""

    type: Required[Literal["ios"]]
    """Type of mobile push credential. Should be <code>ios</code> here"""


class CreateMobilePushCredentialRequestAndroid(TypedDict, total=False):
    alias: Required[str]
    """Alias to uniquely identify the credential"""

    project_account_json_file: Required[Dict[str, object]]
    """Private key file in JSON format"""

    type: Required[Literal["android"]]
    """Type of mobile push credential. Should be <code>android</code> here"""


CreateMobilePushCredentialRequest: TypeAlias = Union[
    CreateMobilePushCredentialRequestIos, CreateMobilePushCredentialRequestAndroid
]
