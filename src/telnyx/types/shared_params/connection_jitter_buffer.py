# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ConnectionJitterBuffer"]


class ConnectionJitterBuffer(TypedDict, total=False):
    """Configuration options for Jitter Buffer.

    Enables Jitter Buffer for RTP streams of SIP Trunking calls. The feature is off unless enabled. You may define min and max values in msec for customized buffering behaviors. Larger values add latency but tolerate more jitter, while smaller values reduce latency but are more sensitive to jitter and reordering.
    """

    enable_jitter_buffer: bool
    """Enables Jitter Buffer for RTP streams of SIP Trunking calls.

    The feature is off unless enabled.
    """

    jitterbuffer_msec_max: int
    """The maximum jitter buffer size in milliseconds.

    Must be between 40 and 400. Has no effect if enable_jitter_buffer is not true.
    """

    jitterbuffer_msec_min: int
    """The minimum jitter buffer size in milliseconds.

    Must be between 40 and 400. Has no effect if enable_jitter_buffer is not true.
    """
