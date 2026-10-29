# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessagingProfileFeatures"]


class MessagingProfileFeatures(BaseModel):
    """
    Telnyx product features the messaging customer can enable on the messaging profile. Keys map to individual feature flags; unknown keys are accepted and preserved for forward compatibility with rolling deployments.
    """

    ai_opt_out_detection_enabled: Optional[bool] = None
    """
    Enables AI detection of inbound opt-out messages that do not follow the standard
    STOP/UNSTOP/HELP opt-out keyword pattern. When enabled, the messaging platform
    applies an AI model to identify non-standard opt-out requests (e.g.
    natural-language phrases) and treats them as opt-outs.
    """

    auto_chunk_long_messages: Optional[bool] = None
    """Enables server-side chunking of outbound SMS.

    When enabled, an outbound message that exceeds the maximum number of segments
    allowed for its destination (10 segments by default; some aggregators accept up
    to 25) is automatically split into multiple child messages, each within the
    segment limit, and sent sequentially in order. Splitting is encoding-aware:
    GSM-7 bodies split at 153-character boundaries and UCS-2 bodies at 134-byte
    (67-character) boundaries. When disabled (the default), messages exceeding the
    segment limit are rejected with an error.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
