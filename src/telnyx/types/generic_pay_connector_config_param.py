# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "GenericPayConnectorConfigParam",
    "BasicAuthenticationAlsoTheValidationDefault",
    "BearerAuthentication",
    "NoProcessorAuthentication",
]


class BasicAuthenticationAlsoTheValidationDefault(TypedDict, total=False):
    password: Required[str]
    """Basic password."""

    username: Required[str]
    """Basic username."""

    token: object
    """Nonblank string required for bearer authentication.

    Write-only; omitted from responses. Re-send when replacing a bearer-auth config.
    """

    auth_type: Literal["basic"]

    endpoint_url: str
    """HTTP or HTTPS processor URL with a host.

    Use HTTPS to protect payment data in transit.
    """

    timeout: Optional[int]
    """Processor HTTP timeout in milliseconds.

    Omitted or null uses 10000; null is removed before storage. Not the IVR
    digit-gather timeout.
    """


class BearerAuthentication(TypedDict, total=False):
    token: Required[str]
    """Processor bearer token."""

    auth_type: Required[Literal["bearer"]]

    endpoint_url: str
    """HTTP or HTTPS processor URL with a host.

    Use HTTPS to protect payment data in transit.
    """

    password: object
    """Nonblank string required for basic authentication.

    Write-only; omitted from responses. Re-send when replacing a basic-auth config.
    """

    timeout: Optional[int]
    """Processor HTTP timeout in milliseconds.

    Omitted or null uses 10000; null is removed before storage. Not the IVR
    digit-gather timeout.
    """

    username: object
    """Nonblank string required for basic authentication.

    Returned in connector responses.
    """


class NoProcessorAuthentication(TypedDict, total=False):
    auth_type: Required[Literal["none"]]

    token: object
    """Nonblank string required for bearer authentication.

    Write-only; omitted from responses. Re-send when replacing a bearer-auth config.
    """

    endpoint_url: str
    """HTTP or HTTPS processor URL with a host.

    Use HTTPS to protect payment data in transit.
    """

    password: object
    """Nonblank string required for basic authentication.

    Write-only; omitted from responses. Re-send when replacing a basic-auth config.
    """

    timeout: Optional[int]
    """Processor HTTP timeout in milliseconds.

    Omitted or null uses 10000; null is removed before storage. Not the IVR
    digit-gather timeout.
    """

    username: object
    """Nonblank string required for basic authentication.

    Returned in connector responses.
    """


GenericPayConnectorConfigParam: TypeAlias = Union[
    BasicAuthenticationAlsoTheValidationDefault, BearerAuthentication, NoProcessorAuthentication
]
