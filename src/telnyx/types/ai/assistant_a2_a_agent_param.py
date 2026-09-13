# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "AssistantA2AAgentParam",
    "Header",
    "Message",
    "MessageA2AAgentRequestStartMessage",
    "MessageA2AAgentRequestResponseDelayedMessage",
]


class Header(TypedDict, total=False):
    """
    A header sent when fetching an A2A agent's card and on every call made to that agent.
    """

    name: Required[str]
    """HTTP header name.

    May only contain alphanumeric characters, hyphens, and underscores, or a
    `{{dynamic_variable}}` placeholder surrounded by those characters.
    """

    value: Required[str]
    """Header value, stored exactly as written.

    It may be a literal, a `{{dynamic_variable}}`, or an
    `{{#integration_secret}}identifier{{/integration_secret}}` section that resolves
    to a stored integration secret when the conversation starts. Control characters
    are not allowed. The encrypted `{{variable | encryption_secret_ref}}` form used
    for per-caller credentials is not resolved here and is rejected when the
    assistant is saved.
    """


class MessageA2AAgentRequestStartMessage(TypedDict, total=False):
    content: Required[str]
    """The text the assistant speaks."""

    type: Required[Literal["request_start"]]
    """Speak the filler message immediately when the call to the agent begins."""

    timing_ms: int
    """An optional delay value. This value is ignored for `request_start` messages."""


class MessageA2AAgentRequestResponseDelayedMessage(TypedDict, total=False):
    content: Required[str]
    """The text the assistant speaks."""

    timing_ms: Required[int]
    """How long to wait, in milliseconds, before speaking this message."""

    type: Required[Literal["request_response_delayed"]]
    """
    Speak the filler message only if the agent has not answered yet after
    `timing_ms`.
    """


Message: TypeAlias = Union[MessageA2AAgentRequestStartMessage, MessageA2AAgentRequestResponseDelayedMessage]

_AssistantA2AAgentParamReservedKeywords = TypedDict(
    "_AssistantA2AAgentParamReservedKeywords",
    {
        "async": bool,
    },
    total=False,
)


class AssistantA2AAgentParam(_AssistantA2AAgentParamReservedKeywords, total=False):
    """
    A remote agent, reachable over the A2A (Agent2Agent) protocol, that an assistant can delegate to. Tools are not configured here: at the start of every conversation the agent's card is fetched and one tool is derived per skill the card advertises.
    """

    name: Required[str]
    """
    Identifies the agent and seeds the names of the tools derived from its card
    (`a2a_<name>_<skill_id>`). Characters outside `[A-Za-z0-9_]` are replaced with
    `_` before the tool name is built, so two agents whose names differ only in
    punctuation collide and are rejected.
    """

    url: Required[str]
    """The agent's base URL, or the URL of its agent card.

    At most 2,048 bytes once UTF-8 encoded. `/.well-known/agent-card.json` is
    appended to the path unless it already ends in `.json`. Must be an `http://` or
    `https://` URL for an externally reachable host: internal destinations
    (`localhost`, private and reserved IP ranges, `.local` domains) are rejected,
    and the hostname may not contain a `{{...}}` placeholder. Placeholders in the
    path are allowed.
    """

    headers: Iterable[Header]
    """Headers sent when fetching this agent's card and on every call made to it.

    Use them to authenticate to the agent.
    """

    messages: Iterable[Message]
    """Filler messages spoken while a call to this agent is in progress.

    `request_start` messages are spoken immediately when the call begins.
    `request_response_delayed` messages are spoken after `timing_ms` has elapsed
    only if the agent has not answered yet. Filler messages are not used when
    `async` is `true`.
    """

    poll_interval_ms: int
    """How often, in milliseconds, to poll an agent task that has not finished yet.

    Defaults to 500.
    """

    timeout_ms: int
    """
    Total budget, in milliseconds, for one call to this agent, including any time
    spent polling a task that is still running. Omit to inherit the assistant's tool
    timeout.
    """
