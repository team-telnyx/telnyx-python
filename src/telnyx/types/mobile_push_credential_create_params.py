# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["MobilePushCredentialCreateParams", "CreateIosPushCredentialRequest", "CreateAndroidPushCredentialRequest"]


class CreateIosPushCredentialRequest(TypedDict, total=False):
    alias: Required[str]
    """Alias to uniquely identify the credential"""

    certificate: Required[str]
    """Certificate as received from APNs"""

    private_key: Required[str]
    """Corresponding private key to the certificate as received from APNs"""

    type: Required[Literal["ios"]]
    """Type of mobile push credential. Should be <code>ios</code> here"""


class CreateAndroidPushCredentialRequest(TypedDict, total=False):
    alias: Required[str]
    """Alias to uniquely identify the credential"""

    project_account_json_file: Required[Dict[str, object]]
    """Private key file in JSON format"""

    type: Required[Literal["android"]]
    """Type of mobile push credential. Should be <code>android</code> here"""


MobilePushCredentialCreateParams: TypeAlias = Union[CreateIosPushCredentialRequest, CreateAndroidPushCredentialRequest]
