# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ActionStopForkingParams"]


class ActionStopForkingParams(TypedDict, total=False):
    client_state: str
    """Use this field to add state to every subsequent webhook.

    It must be a valid Base-64 encoded string.
    """

    command_id: str
    """Use this field to avoid duplicate commands.

    Telnyx will ignore any command with the same `command_id` for the same
    `call_control_id`.
    """

    stream_type: Literal["raw", "decrypted"]
    """Optionally specify a `stream_type`.

    This should match the `stream_type` that was used in `fork_start` command to
    properly stop the fork.
    """
