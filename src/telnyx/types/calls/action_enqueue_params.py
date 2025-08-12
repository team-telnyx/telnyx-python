# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ActionEnqueueParams"]


class ActionEnqueueParams(TypedDict, total=False):
    queue_name: Required[str]
    """The name of the queue the call should be put in.

    If a queue with a given name doesn't exist yet it will be created.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    max_size: int
    """The maximum number of calls allowed in the queue at a given time.

    Can't be modified for an existing queue.
    """

    max_wait_time_secs: int
    """The number of seconds after which the call will be removed from the queue."""
