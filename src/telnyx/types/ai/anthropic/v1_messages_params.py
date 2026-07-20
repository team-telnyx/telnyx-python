# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["V1MessagesParams"]


class V1MessagesParams(TypedDict, total=False):
    max_tokens: Required[int]
    """The maximum number of tokens to generate in the response."""

    messages: Required[Iterable[Dict[str, object]]]
    """
    The messages to send to the model, following the
    [Anthropic Messages API](https://docs.anthropic.com/en/api/messages) format.
    """

    model: Required[str]
    """
    The model to use for generating the response, for example `zai-org/GLM-5.2` or
    another model available from the Telnyx models endpoint.
    """

    api_key_ref: str
    """
    If you are using an external inference provider, this field allows you to pass
    along a reference to your API key. After creating an
    [integration secret](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret)
    for your API key, pass the secret's `identifier` in this field.
    """

    billing_group_id: str
    """The billing group ID to associate with this request."""

    fallback_config: Dict[str, object]
    """
    Configuration for model fallback behavior when the primary model is unavailable.
    """

    max_retries: int
    """Maximum number of retries for the request."""

    mcp_servers: Iterable[Dict[str, object]]
    """List of MCP (Model Context Protocol) servers to make available to the model."""

    metadata: Dict[str, object]
    """An object describing metadata about the request."""

    service_tier: str
    """Service tier for the request."""

    stop_sequences: SequenceNotStr[str]
    """Custom sequences that will cause the model to stop generating."""

    stream: bool
    """Whether to stream the response as Anthropic-format Server-Sent Events."""

    system: Union[str, Iterable[Dict[str, object]]]
    """System prompt.

    Can be a string or an array of content blocks following the Anthropic API
    format.
    """

    temperature: float
    """Amount of randomness injected into the response. Ranges from 0 to 1."""

    thinking: Dict[str, object]
    """Extended thinking configuration for models that support it.

    Set `type` to `enabled` to turn on extended thinking.
    """

    api_timeout: Annotated[float, PropertyInfo(alias="timeout")]
    """Request timeout in seconds."""

    tool_choice: Dict[str, object]
    """Controls how the model uses tools, following the Anthropic API format."""

    tools: Iterable[Dict[str, object]]
    """
    Definitions of tools that the model may use, following the Anthropic API format.
    """

    top_k: int
    """Top-k sampling parameter.

    Only sample from the top K options for each subsequent token.
    """

    top_p: float
    """Nucleus sampling parameter. Use temperature or top_p, but not both."""
