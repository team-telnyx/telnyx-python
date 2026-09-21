# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PostConversationSettingsReqParam"]


class PostConversationSettingsReqParam(TypedDict, total=False):
    """Configuration for post-conversation processing.

    When enabled, the assistant receives one additional LLM turn after the conversation ends, allowing it to execute final tool calls such as sending a summary or updating a record via webhook or function tools. Integration and MCP server tools are not available post-conversation; call-control tools (e.g. hangup, transfer) are also unavailable. Beta feature.
    """

    enabled: bool
    """Whether post-conversation processing is enabled.

    When true, the assistant will be invoked after the conversation ends to perform
    any final tool calls. Defaults to false.
    """
