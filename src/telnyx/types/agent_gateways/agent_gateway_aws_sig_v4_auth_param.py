# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AgentGatewayAwsSigV4AuthParam"]


class AgentGatewayAwsSigV4AuthParam(TypedDict, total=False):
    """The gateway signs each request with AWS Signature Version 4.

    Without keys or a role, it uses the instance's own AWS identity. Keys are write-only.
    """

    region: Required[str]
    """The AWS region to sign for."""

    type: Required[Literal["aws_sigv4"]]

    access_key_id: Optional[str]

    role_name: Optional[str]
    """The ARN of a role for the gateway to assume."""

    secret_access_key: Optional[str]

    service: str
    """The AWS service to sign for."""

    session_token: Optional[str]
