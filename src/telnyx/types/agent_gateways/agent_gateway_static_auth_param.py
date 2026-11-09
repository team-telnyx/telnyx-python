# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentGatewayStaticAuthParam"]


class AgentGatewayStaticAuthParam(TypedDict, total=False):
    """A static credential the gateway sends on every request.

    Write-only: responses show its `type` only.
    """

    type: Required[Literal["api_key", "bearer_token", "basic", "token", "authorization"]]
    """
    How the credential is sent: `api_key` as `X-API-Key: <value>`, `bearer_token` as
    `Authorization: Bearer <value>`, `basic` as
    `Authorization: Basic <base64 of value>` with `value` in the form
    `user:password`, `token` as `Authorization: token <value>`, and `authorization`
    as `Authorization: <value>`.
    """

    value: Required[str]
    """The credential."""

    header: Optional[str]
    """A header name that replaces `X-API-Key` or `Authorization`."""
