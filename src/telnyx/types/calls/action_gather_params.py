# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ActionGatherParams"]


class ActionGatherParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    gather_id: str
    """An id that will be sent back in the corresponding `call.gather.ended` webhook.

    Will be randomly generated if not specified.
    """

    initial_timeout_millis: int
    """The number of milliseconds to wait for the first DTMF."""

    inter_digit_timeout_millis: int
    """The number of milliseconds to wait for input between digits."""

    maximum_digits: int
    """The maximum number of digits to fetch.

    This parameter has a maximum value of 128.
    """

    minimum_digits: int
    """The minimum number of digits to fetch. This parameter has a minimum value of 1."""

    terminating_digit: str
    """
    The digit used to terminate input if fewer than `maximum_digits` digits have
    been gathered.
    """

    timeout_millis: int
    """The number of milliseconds to wait to complete the request."""

    valid_digits: str
    """A list of all digits accepted as valid."""
