# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ConnectionJitterBuffer"]


class ConnectionJitterBuffer(BaseModel):
    """Configuration options for Jitter Buffer.

    Enables Jitter Buffer for RTP streams of SIP Trunking calls. The feature is off unless enabled. You may define min and max values in msec for customized buffering behaviors. Larger values add latency but tolerate more jitter, while smaller values reduce latency but are more sensitive to jitter and reordering.
    """

    enable_jitter_buffer: Optional[bool] = None
    """Enables Jitter Buffer for RTP streams of SIP Trunking calls.

    The feature is off unless enabled.
    """

    jitterbuffer_msec_max: Optional[int] = None
    """The maximum jitter buffer size in milliseconds.

    Must be between 40 and 400. Has no effect if enable_jitter_buffer is not true.
    """

    jitterbuffer_msec_min: Optional[int] = None
    """The minimum jitter buffer size in milliseconds.

    Must be between 40 and 400. Has no effect if enable_jitter_buffer is not true.
    """
