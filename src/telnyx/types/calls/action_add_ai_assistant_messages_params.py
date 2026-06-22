# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import TypeAlias, TypedDict

from .tool_message_param import ToolMessageParam
from .user_message_param import UserMessageParam
from .system_message_param import SystemMessageParam
from .assistant_message_param import AssistantMessageParam
from .developer_message_param import DeveloperMessageParam

__all__ = ["ActionAddAIAssistantMessagesParams", "Message"]


class ActionAddAIAssistantMessagesParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    messages: Iterable[Message]
    """The messages to add to the conversation."""


Message: TypeAlias = Union[
    UserMessageParam, AssistantMessageParam, ToolMessageParam, SystemMessageParam, DeveloperMessageParam
]
