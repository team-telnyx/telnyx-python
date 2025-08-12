# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IntegrationSecretCreateParams"]


class IntegrationSecretCreateParams(TypedDict, total=False):
    identifier: Required[str]
    """The unique identifier of the secret."""

    type: Required[Literal["bearer", "basic"]]
    """The type of secret."""

    token: str
    """The token for the secret. Required for bearer type secrets, ignored otherwise."""

    password: str
    """The password for the secret.

    Required for basic type secrets, ignored otherwise.
    """

    username: str
    """The username for the secret.

    Required for basic type secrets, ignored otherwise.
    """
