# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MessagingProfileFeaturesParam"]


class MessagingProfileFeaturesParam(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    """
    Telnyx product features the messaging customer can enable on the messaging profile. Keys map to individual feature flags; unknown keys are accepted and preserved for forward compatibility with rolling deployments.
    """

    ai_opt_out_detection_enabled: bool
    """
    Enables AI detection of inbound opt-out messages that do not follow the standard
    STOP/UNSTOP/HELP opt-out keyword pattern. When enabled, the messaging platform
    applies an AI model to identify non-standard opt-out requests (e.g.
    natural-language phrases) and treats them as opt-outs.
    """

    auto_chunk_long_messages: bool
    """Enables server-side chunking of outbound SMS.

    When enabled, an outbound message that exceeds the maximum number of segments
    allowed for its destination (10 segments by default; some aggregators accept up
    to 25) is automatically split into multiple child messages, each within the
    segment limit, and sent sequentially in order. Splitting is encoding-aware:
    GSM-7 bodies split at 153-character boundaries and UCS-2 bodies at 134-character
    boundaries. When disabled (the default), messages exceeding the segment limit
    are rejected with an error.
    """
