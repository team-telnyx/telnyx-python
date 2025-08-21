# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ActionUpdateParams"]


class ActionUpdateParams(TypedDict, total=False):
    call_control_id: Required[str]
    """Unique identifier and token for controlling the call"""

    supervisor_role: Required[Literal["barge", "monitor", "none", "whisper"]]
    """Sets the participant as a supervisor for the conference.

    A conference can have multiple supervisors. "barge" means the supervisor enters
    the conference as a normal participant. This is the same as "none". "monitor"
    means the supervisor is muted but can hear all participants. "whisper" means
    that only the specified "whisper_call_control_ids" can hear the supervisor.
    Defaults to "none".
    """

    command_id: str
    """Use this field to avoid execution of duplicate commands.

    Telnyx will ignore subsequent commands with the same `command_id` as one that
    has already been executed.
    """

    whisper_call_control_ids: List[str]
    """Array of unique call_control_ids the supervisor can whisper to.

    If none provided, the supervisor will join the conference as a monitoring
    participant only.
    """
