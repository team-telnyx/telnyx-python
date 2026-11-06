# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Union, Optional, ForwardRef
from typing_extensions import Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = ["APICreateParams", "Auth"]


class APICreateParams(TypedDict, total=False):
    name: Required[str]
    """
    A name for the API, unique on the instance across MCP servers and APIs,
    regardless of case. Up to 100 letters, digits, `_`, and `.`. The gateway
    prefixes the API's tools with it and a hyphen.
    """

    spec_url: Required[str]
    """
    The URL of the API's OpenAPI description: OpenAPI 3.0, OpenAPI 3.1, or Swagger
    2.0.
    """

    auth: Auth
    """How the gateway authenticates to the API.

    AWS Signature Version 4 is for MCP servers only. Replaced whole on an update.
    """

    base_url: Optional[str]
    """Where the gateway sends the API's requests.

    Without it, the gateway takes the description's first `servers` entry.
    """

    forwarded_headers: SequenceNotStr[str]
    """Headers copied from the agent's request, by name."""

    open_to_every_key: bool
    """`true` lets every key on the instance use the server, granted or not."""

    static_headers: Dict[str, str]
    """Headers sent on every request."""

    tools: SequenceNotStr[str]
    """The operations the API exposes as tools, by tool name.

    `[]` exposes every operation.
    """


if TYPE_CHECKING:
    Auth: TypeAlias = Union[
        "AgentGatewayNoAuthParam",
        "AgentGatewayStaticAuthParam",
        "AgentGatewayOAuthClientCredentialsParam",
        "AgentGatewayPassthroughAuthParam",
    ]
else:
    Auth = Union[
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AgentGatewayNoAuthParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AgentGatewayStaticAuthParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AgentGatewayOAuthClientCredentialsParam"),
        ForwardRef(f"__import__({__name__!r}, fromlist=('',)).AgentGatewayPassthroughAuthParam"),
    ]

from .agent_gateway_no_auth_param import AgentGatewayNoAuthParam
from .agent_gateway_static_auth_param import AgentGatewayStaticAuthParam
from .agent_gateway_passthrough_auth_param import AgentGatewayPassthroughAuthParam
from .agent_gateway_oauth_client_credentials_param import AgentGatewayOAuthClientCredentialsParam
