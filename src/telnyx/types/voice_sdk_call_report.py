# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .voice_sdk_call_report_log_entry import VoiceSDKCallReportLogEntry

__all__ = ["VoiceSDKCallReport", "Logs", "LogsEntries", "Stats", "StatsUnionMember1"]


class LogsEntries(BaseModel):
    """
    Raw logs object emitted by the Voice SDK when logs are grouped under an entries field.
    """

    entries: Optional[List[VoiceSDKCallReportLogEntry]] = None
    """Raw log entries when the SDK groups logs under an entries field."""

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


Logs: TypeAlias = Union[List[VoiceSDKCallReportLogEntry], LogsEntries]


class StatsUnionMember1(BaseModel):
    """Raw stats object emitted by the Voice SDK."""

    audio: Optional[Dict[str, object]] = None
    """
    Raw audio stats such as inbound/outbound packet, byte, jitter, packet-loss,
    bitrate, and audio-level metrics.
    """

    connection: Optional[Dict[str, object]] = None
    """
    Raw connection stats such as round-trip time, packets, and bytes sent or
    received.
    """

    ice: Optional[Dict[str, object]] = None
    """
    Raw ICE candidate-pair information, including selected pair, local/remote
    candidates, state, and nomination data when provided by the SDK.
    """

    transport: Optional[Dict[str, object]] = None
    """
    Raw transport stats such as ICE state, DTLS state, SRTP cipher, TLS version, and
    selected-candidate-pair changes.
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


Stats: TypeAlias = Union[List[Dict[str, object]], StatsUnionMember1]


class VoiceSDKCallReport(BaseModel):
    """A raw call report stats JSON payload.

    The schema is intentionally permissive because Voice SDK clients can add fields over time.
    """

    call_id: Optional[str] = None
    """Unique call identifier."""

    call_report_id: Optional[str] = None
    """User-scoped storage grouping identifier derived from the authenticated user.

    This is not a unique per-call report identifier and may be shared by multiple
    calls for the same user.
    """

    created_at: Optional[datetime] = None
    """Creation timestamp when present."""

    flush_reason: Optional[Dict[str, object]] = FieldInfo(alias="flushReason", default=None)
    """
    Reason the SDK flushed this stats report segment, for example an intermediate
    socket-close flush.
    """

    logs: Optional[Logs] = None
    """Raw logs payload emitted by the Voice SDK and stored without normalization.

    Live responses commonly return an array of log entries, but object-shaped log
    payloads are also allowed for compatibility.
    """

    organization_id: Optional[str] = None
    """
    Organization associated with the stored call report when provided by the Voice
    SDK reporting path.
    """

    segment: Optional[int] = None
    """
    Zero-based stats segment index when the SDK sends segmented or intermediate
    reports.
    """

    stats: Optional[Stats] = None
    """Raw stats payload emitted by the Voice SDK and stored without normalization.

    The exact shape can vary by SDK platform and version. Live responses commonly
    return an array of interval snapshots, but object-shaped stats payloads are also
    allowed for compatibility.
    """

    stored_at: Optional[datetime] = None
    """Time when the call report was stored."""

    summary: Optional[Dict[str, object]] = None
    """High-level call metadata."""

    telnyx_leg_id: Optional[str] = None
    """
    Telnyx call leg identifier for correlating the report with call-control, SIP,
    and media troubleshooting data.
    """

    telnyx_session_id: Optional[str] = None
    """
    Telnyx RTC session identifier for correlating the report with Voice SDK
    signaling and media-session logs.
    """

    user_agent: Optional[str] = None
    """Voice SDK user agent string reported by the client.

    This is the preferred SDK/platform/version dimension when present.
    """

    user_id: Optional[str] = None
    """Authenticated user that owns the call report."""

    version: Optional[str] = None
    """
    Legacy SDK version value when the client reports one separately from the user
    agent.
    """

    voice_sdk_id: Optional[str] = None
    """Voice SDK instance identifier."""

    voice_sdk_id_decoded: Optional[Dict[str, object]] = None
    """
    Decoded Voice SDK identifier metadata emitted by voice-sdk-proxy when available.
    """

    voice_sdk_session_id: Optional[str] = None
    """
    Voice SDK session correlation identifier used to group stats segments for the
    same SDK session.
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
