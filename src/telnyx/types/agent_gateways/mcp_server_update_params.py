# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, ForwardRef
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["McpServerUpdateParams", "Auth"]


class McpServerUpdateParams(TypedDict, total=False):
    instance_id: Required[str]

    auth: Auth
    """How the gateway authenticates to the server.

    Replaced whole on an update; `{"type": "none"}` removes the credential.
    """

    forwarded_headers: SequenceNotStr[str]
    """Headers copied from the agent's request, by name."""

    name: str
    """
    A name for the server, unique on the instance across MCP servers and APIs,
    regardless of case. Letters, digits, `_`, and `.`. The gateway prefixes the
    server's tools with it and a hyphen.
    """

    open_to_every_key: bool
    """`true` lets every key on the instance use the server, granted or not."""

    static_headers: Dict[str, str]
    """Headers sent on every request."""

    tools: SequenceNotStr[str]
    """The tools the server exposes to every key, by name. `[]` exposes every tool."""

    transport: Literal["http", "sse"]
    """`http` for Streamable HTTP, or `sse` for Server-Sent Events."""

    url: str
    """The server's MCP endpoint, `http` or `https`."""


if TYPE_CHECKING:
    Auth: TypeAlias = Union[
        "AgentGatewayNoAuthParam",
        "AgentGatewayStaticAuthParam",
        "AgentGatewayOAuthClientCredentialsParam",
        "AgentGatewayPassthroughAuthParam",
        "AgentGatewayAwsSigV4AuthParam",
    ]
else:
    Auth = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AgentGatewayNoAuthParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AgentGatewayStaticAuthParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AgentGatewayOAuthClientCredentialsParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AgentGatewayPassthroughAuthParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AgentGatewayAwsSigV4AuthParam"),
    ]

from .agent_gateway_no_auth_param import AgentGatewayNoAuthParam
from .agent_gateway_static_auth_param import AgentGatewayStaticAuthParam
from .agent_gateway_aws_sig_v4_auth_param import AgentGatewayAwsSigV4AuthParam
from .agent_gateway_passthrough_auth_param import AgentGatewayPassthroughAuthParam
from .agent_gateway_oauth_client_credentials_param import AgentGatewayOAuthClientCredentialsParam
