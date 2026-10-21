# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Required, TypedDict

__all__ = ["TtsIntegrationCreateParams"]


class TtsIntegrationCreateParams(TypedDict, total=False):
    capabilities: Required["CommunityTtsEngineCapabilitiesParam"]
    """What the engine supports. An unknown key is rejected."""

    name: Required[str]
    """The engine's unique name, and the first part of its voices
    (`<name>.<voice_id>`).

    1-64 characters: lowercase letters, digits, hyphens and underscores, starting
    with a letter or digit. Built-in vendor names and the generic voice names
    `male`, `female`, `man`, `woman`, `alice` and `custom` are reserved. Unique
    across all Telnyx accounts and cannot be changed later. A deleted engine's name
    stays reserved for the organization that owned it.
    """

    supported_audio_formats: Required[List["CommunityTtsAudioFormat"]]
    """The audio formats the engine can produce, at least one, without duplicates."""

    voices_url: Required[str]
    """The `https://` URL of the engine's voice listing, with the same host rules.

    It answers `GET` with
    `{"voices": [{"provider", "name", "voice_id", "language", "gender"}]}`: at most
    1000 voices, each `voice_id` unique and matching
    `^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$`, each `language` at most 35 characters.
    Telnyx reads it when the engine is registered or updated, every 15 minutes, and
    on `refresh_voices`.
    """

    websocket_url: Required[str]
    """The `wss://` URL Telnyx connects to.

    It must be reachable on the public internet: plain `ws://`, private, loopback,
    link-local, shared, documentation, multicast and reserved addresses, and
    internal hostnames are rejected, as are credentials embedded in the URL or in
    credential-looking query parameters. At most 2048 characters.
    """

    connect_timeout_ms: int
    """How long Telnyx waits for the WebSocket connection to open, from 500 to 10000.

    Default: 3000.
    """

    contact_email: Optional[str]
    """A contact address stored for the Telnyx platform team.

    Telnyx does not email it automatically. At most 254 characters.
    """

    data_retention_policy_url: Optional[str]
    """URL of the publisher's data retention policy, at most 2048 characters.

    It is returned in the discoverable listing.
    """

    documentation_url: Optional[str]
    """
    An `https://` page where callers learn how to get a key for the engine and how
    to use it, with a host and no credentials in it, at most 2048 characters. It is
    returned in the discoverable listing.
    """

    visibility: "CommunityTtsEngineVisibility"
    """`private`: only your organization can use the engine.

    `public`: any organization can, once it is `active`.
    """

    voices_api_key_ref: Optional[str]
    """The identifier of an Integration Secret in your organization.

    When set, Telnyx sends its value as a bearer token when it reads `voices_url`.
    It is never used for synthesis. Send `null` on an update to clear it. At most
    255 characters.
    """


from .community_tts_audio_format import CommunityTtsAudioFormat
from .community_tts_engine_visibility import CommunityTtsEngineVisibility
from .community_tts_engine_capabilities_param import CommunityTtsEngineCapabilitiesParam
