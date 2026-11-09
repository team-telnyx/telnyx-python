# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["AgentGatewayOAuthClientCredentialsParam"]


class AgentGatewayOAuthClientCredentialsParam(TypedDict, total=False):
    """
    The gateway gets its own access token with the `client_credentials` grant and sends it as a bearer token on every request, renewing it before it expires. The client ID and secret are write-only.
    """

    client_id: Required[str]

    client_secret: Required[str]

    token_url: Required[str]
    """The OAuth provider's token endpoint."""

    type: Required[Literal["oauth_client_credentials"]]

    audience: Optional[str]
    """The token's audience, sent in the token request."""

    credentials_in: Literal["body", "basic"]
    """
    Whether the client ID and secret go in the token request's body or as HTTP Basic
    authentication.
    """

    resource: Optional[str]
    """The resource the token is for, sent in the token request."""

    scopes: SequenceNotStr[str]
    """The scopes to request."""
