# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ActionSendDtmfParams"]


class ActionSendDtmfParams(TypedDict, total=False):
    digits: Required[str]
    """DTMF digits to send.

    Valid characters: 0-9, A-D, \\**, #, w (0.5s pause), W (1s pause).
    """

    call_control_ids: SequenceNotStr[str]
    """Array of participant call control IDs to send DTMF to.

    When empty, DTMF will be sent to all participants.
    """

    client_state: str
    """Use this field to add state to every subsequent webhook.

    Must be a valid Base-64 encoded string.
    """

    duration_millis: int
    """Duration of each DTMF digit in milliseconds."""
