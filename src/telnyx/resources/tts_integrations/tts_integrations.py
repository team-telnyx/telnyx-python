# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ...types import (
    CommunityTtsEngineStatus,
    CommunityTtsEngineVisibility,
    tts_integration_list_params,
    tts_integration_create_params,
    tts_integration_update_params,
    tts_integration_replace_params,
    tts_integration_retrieve_discoverable_params,
    tts_integration_retrieve_conformance_runs_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.community_tts_engine import CommunityTtsEngine
from ...types.community_tts_audio_format import CommunityTtsAudioFormat
from ...types.community_tts_engine_status import CommunityTtsEngineStatus
from ...types.tts_integration_list_response import TtsIntegrationListResponse
from ...types.community_tts_engine_visibility import CommunityTtsEngineVisibility
from ...types.community_tts_engine_capabilities_param import CommunityTtsEngineCapabilitiesParam
from ...types.tts_integration_retrieve_voices_response import TtsIntegrationRetrieveVoicesResponse
from ...types.tts_integration_retrieve_discoverable_response import TtsIntegrationRetrieveDiscoverableResponse
from ...types.tts_integration_retrieve_conformance_runs_response import TtsIntegrationRetrieveConformanceRunsResponse

__all__ = ["TtsIntegrationsResource", "AsyncTtsIntegrationsResource"]


class TtsIntegrationsResource(SyncAPIResource):
    """
    Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
    """

    @cached_property
    def actions(self) -> ActionsResource:
        """
        Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
        """
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TtsIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TtsIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TtsIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TtsIntegrationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        capabilities: CommunityTtsEngineCapabilitiesParam,
        name: str,
        supported_audio_formats: List[CommunityTtsAudioFormat],
        voices_url: str,
        websocket_url: str,
        connect_timeout_ms: int | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        data_retention_policy_url: Optional[str] | Omit = omit,
        documentation_url: Optional[str] | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        voices_api_key_ref: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsEngine:
        """Register a WebSocket text-to-speech engine.

        Telnyx reads the engine's
        `voices_url` while it registers the engine and refuses the registration with a
        `422` if the list is unreachable or invalid. The engine starts at
        `status: draft` and cannot serve other organizations' traffic until Telnyx
        approves it (your own organization can try it with its own key meanwhile). It is
        `visibility: private` unless you set `public`: a private engine can be used only
        by your organization, a public one by any organization once it is `active`. See
        the [Community TTS engines guide](/docs/voice/tts/community-engines) for the
        full review flow.

        `websocket_url` must be `wss://` and `voices_url` must be `https://`, both on a
        public host; a plain `ws://` URL is rejected, and so is a credential embedded in
        either. Callers bring their own key for your engine: Telnyx stores none, so
        there is nothing to register here for synthesis. `voices_api_key_ref` is
        optional and used only to read your voice list.

        Args:
          capabilities: What the engine supports. An unknown key is rejected.

          name: The engine's unique name, and the first part of its voices
              (`<name>.<voice_id>`). 1-64 characters: lowercase letters, digits, hyphens and
              underscores, starting with a letter or digit. Built-in vendor names and the
              generic voice names `male`, `female`, `man`, `woman`, `alice` and `custom` are
              reserved. Unique across all Telnyx accounts and cannot be changed later. A
              deleted engine's name stays reserved for the organization that owned it.

          supported_audio_formats: The audio formats the engine can produce, at least one, without duplicates.

          voices_url: The `https://` URL of the engine's voice listing, with the same host rules. It
              answers `GET` with
              `{"voices": [{"provider", "name", "voice_id", "language", "gender"}]}`: at most
              1000 voices, each `voice_id` unique and matching
              `^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$`, each `language` at most 35 characters.
              Telnyx reads it when the engine is registered or updated, every 15 minutes, and
              on `refresh_voices`.

          websocket_url: The `wss://` URL Telnyx connects to. It must be reachable on the public
              internet: plain `ws://`, private, loopback, link-local, shared, documentation,
              multicast and reserved addresses, and internal hostnames are rejected, as are
              credentials embedded in the URL or in credential-looking query parameters. At
              most 2048 characters.

          connect_timeout_ms: How long Telnyx waits for the WebSocket connection to open, from 500 to 10000.
              Default: 3000.

          contact_email: A contact address stored for the Telnyx platform team. Telnyx does not email it
              automatically. At most 254 characters.

          data_retention_policy_url: URL of the publisher's data retention policy, at most 2048 characters. It is
              returned in the discoverable listing.

          documentation_url: An `https://` page where callers learn how to get a key for the engine and how
              to use it, with a host and no credentials in it, at most 2048 characters. It is
              returned in the discoverable listing.

          visibility: `private`: only your organization can use the engine. `public`: any organization
              can, once it is `active`.

          voices_api_key_ref: The identifier of an Integration Secret in your organization. When set, Telnyx
              sends its value as a bearer token when it reads `voices_url`. It is never used
              for synthesis. Send `null` on an update to clear it. At most 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tts_integrations",
            body=maybe_transform(
                {
                    "capabilities": capabilities,
                    "name": name,
                    "supported_audio_formats": supported_audio_formats,
                    "voices_url": voices_url,
                    "websocket_url": websocket_url,
                    "connect_timeout_ms": connect_timeout_ms,
                    "contact_email": contact_email,
                    "data_retention_policy_url": data_retention_policy_url,
                    "documentation_url": documentation_url,
                    "visibility": visibility,
                    "voices_api_key_ref": voices_api_key_ref,
                },
                tts_integration_create_params.TtsIntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsEngine:
        """
        Retrieve one of your own community TTS engines by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/tts_integrations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    def update(
        self,
        id: str,
        *,
        capabilities: CommunityTtsEngineCapabilitiesParam | Omit = omit,
        connect_timeout_ms: int | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        data_retention_policy_url: Optional[str] | Omit = omit,
        documentation_url: Optional[str] | Omit = omit,
        supported_audio_formats: List[CommunityTtsAudioFormat] | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        voices_api_key_ref: Optional[str] | Omit = omit,
        voices_url: str | Omit = omit,
        websocket_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsEngine:
        """
        Same as `PUT`: only the fields you send change.

        Args:
          capabilities: What the engine supports. An unknown key is rejected.

          visibility: `private`: only your organization can use the engine. `public`: any organization
              can, once it is `active`.

          voices_url: See the create request.

          websocket_url: See the create request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/tts_integrations/{id}", id=id),
            body=maybe_transform(
                {
                    "capabilities": capabilities,
                    "connect_timeout_ms": connect_timeout_ms,
                    "contact_email": contact_email,
                    "data_retention_policy_url": data_retention_policy_url,
                    "documentation_url": documentation_url,
                    "supported_audio_formats": supported_audio_formats,
                    "visibility": visibility,
                    "voices_api_key_ref": voices_api_key_ref,
                    "voices_url": voices_url,
                    "websocket_url": websocket_url,
                },
                tts_integration_update_params.TtsIntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    def list(
        self,
        *,
        page: tts_integration_list_params.Page | Omit = omit,
        status: CommunityTtsEngineStatus | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TtsIntegrationListResponse:
        """
        List every community TTS engine your organization has registered, at any status
        or visibility. Use `GET /tts_integrations/discoverable` instead to also see
        other organizations' public, active engines.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          status: Filter by status.

          visibility: Filter by visibility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/tts_integrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "status": status,
                        "visibility": visibility,
                    },
                    tts_integration_list_params.TtsIntegrationListParams,
                ),
            ),
            cast_to=TtsIntegrationListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete one of your own community TTS engines.

        The engine disappears from every
        listing and lookup and can no longer serve traffic, but its `name` stays
        reserved for your organization: no other organization can register it, and you
        can register it again later. An assistant or call still configured with one of
        its voices cannot use it until an engine with that name exists again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/tts_integrations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def replace(
        self,
        id: str,
        *,
        capabilities: CommunityTtsEngineCapabilitiesParam | Omit = omit,
        connect_timeout_ms: int | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        data_retention_policy_url: Optional[str] | Omit = omit,
        documentation_url: Optional[str] | Omit = omit,
        supported_audio_formats: List[CommunityTtsAudioFormat] | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        voices_api_key_ref: Optional[str] | Omit = omit,
        voices_url: str | Omit = omit,
        websocket_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsEngine:
        """Change one of your own community TTS engines.

        Every field is optional: omit a
        field to leave it unchanged. `name` cannot be changed. Telnyx reads the
        `voices_url` again and refuses an update that leaves the engine with an
        unreadable list. Changing `websocket_url`, `voices_url`,
        `supported_audio_formats` or `capabilities`, or making a `private` engine
        `public`, sends the engine back to `status: draft` and clears its review. See
        the [Community TTS engines guide](/docs/voice/tts/community-engines) for the
        full review flow.

        Args:
          capabilities: What the engine supports. An unknown key is rejected.

          visibility: `private`: only your organization can use the engine. `public`: any organization
              can, once it is `active`.

          voices_url: See the create request.

          websocket_url: See the create request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            path_template("/tts_integrations/{id}", id=id),
            body=maybe_transform(
                {
                    "capabilities": capabilities,
                    "connect_timeout_ms": connect_timeout_ms,
                    "contact_email": contact_email,
                    "data_retention_policy_url": data_retention_policy_url,
                    "documentation_url": documentation_url,
                    "supported_audio_formats": supported_audio_formats,
                    "visibility": visibility,
                    "voices_api_key_ref": voices_api_key_ref,
                    "voices_url": voices_url,
                    "websocket_url": websocket_url,
                },
                tts_integration_replace_params.TtsIntegrationReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    def retrieve_conformance_runs(
        self,
        id: str,
        *,
        page: tts_integration_retrieve_conformance_runs_params.Page | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TtsIntegrationRetrieveConformanceRunsResponse:
        """
        The recorded runs of `test_connection` for one of your engines, newest first.
        Telnyx keeps the latest 50.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/tts_integrations/{id}/conformance_runs", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"page": page},
                    tts_integration_retrieve_conformance_runs_params.TtsIntegrationRetrieveConformanceRunsParams,
                ),
            ),
            cast_to=TtsIntegrationRetrieveConformanceRunsResponse,
        )

    def retrieve_discoverable(
        self,
        *,
        page: tts_integration_retrieve_discoverable_params.Page | Omit = omit,
        status: CommunityTtsEngineStatus | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TtsIntegrationRetrieveDiscoverableResponse:
        """
        List the engines you can use: your own, at any status, and other organizations'
        engines that are `public` and `active`. Each entry carries what a caller needs
        to choose an engine: its `name` (the first part of its voices,
        `<name>.<voice_id>`), `voices_count`, audio formats, capabilities, and
        `documentation_url`. It never carries the publisher's contact details, review
        notes, or `voices_api_key_ref`. Read an engine's voices with
        `GET /tts_integrations/{id}/voices`.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          status: Filter by status.

          visibility: Filter by visibility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/tts_integrations/discoverable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "status": status,
                        "visibility": visibility,
                    },
                    tts_integration_retrieve_discoverable_params.TtsIntegrationRetrieveDiscoverableParams,
                ),
            ),
            cast_to=TtsIntegrationRetrieveDiscoverableResponse,
        )

    def retrieve_voices(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TtsIntegrationRetrieveVoicesResponse:
        """
        The voices Telnyx last read from the engine's `voices_url`, in the shape the
        engine published. A caller selects one as `<engine name>.<voice_id>`. The list
        is replaced only when a new read succeeds, so an engine whose `voices_url` is
        down keeps serving its last list. `[]` until the first read succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/tts_integrations/{id}/voices", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TtsIntegrationRetrieveVoicesResponse,
        )


class AsyncTtsIntegrationsResource(AsyncAPIResource):
    """
    Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
    """

    @cached_property
    def actions(self) -> AsyncActionsResource:
        """
        Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
        """
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTtsIntegrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTtsIntegrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTtsIntegrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTtsIntegrationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        capabilities: CommunityTtsEngineCapabilitiesParam,
        name: str,
        supported_audio_formats: List[CommunityTtsAudioFormat],
        voices_url: str,
        websocket_url: str,
        connect_timeout_ms: int | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        data_retention_policy_url: Optional[str] | Omit = omit,
        documentation_url: Optional[str] | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        voices_api_key_ref: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsEngine:
        """Register a WebSocket text-to-speech engine.

        Telnyx reads the engine's
        `voices_url` while it registers the engine and refuses the registration with a
        `422` if the list is unreachable or invalid. The engine starts at
        `status: draft` and cannot serve other organizations' traffic until Telnyx
        approves it (your own organization can try it with its own key meanwhile). It is
        `visibility: private` unless you set `public`: a private engine can be used only
        by your organization, a public one by any organization once it is `active`. See
        the [Community TTS engines guide](/docs/voice/tts/community-engines) for the
        full review flow.

        `websocket_url` must be `wss://` and `voices_url` must be `https://`, both on a
        public host; a plain `ws://` URL is rejected, and so is a credential embedded in
        either. Callers bring their own key for your engine: Telnyx stores none, so
        there is nothing to register here for synthesis. `voices_api_key_ref` is
        optional and used only to read your voice list.

        Args:
          capabilities: What the engine supports. An unknown key is rejected.

          name: The engine's unique name, and the first part of its voices
              (`<name>.<voice_id>`). 1-64 characters: lowercase letters, digits, hyphens and
              underscores, starting with a letter or digit. Built-in vendor names and the
              generic voice names `male`, `female`, `man`, `woman`, `alice` and `custom` are
              reserved. Unique across all Telnyx accounts and cannot be changed later. A
              deleted engine's name stays reserved for the organization that owned it.

          supported_audio_formats: The audio formats the engine can produce, at least one, without duplicates.

          voices_url: The `https://` URL of the engine's voice listing, with the same host rules. It
              answers `GET` with
              `{"voices": [{"provider", "name", "voice_id", "language", "gender"}]}`: at most
              1000 voices, each `voice_id` unique and matching
              `^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$`, each `language` at most 35 characters.
              Telnyx reads it when the engine is registered or updated, every 15 minutes, and
              on `refresh_voices`.

          websocket_url: The `wss://` URL Telnyx connects to. It must be reachable on the public
              internet: plain `ws://`, private, loopback, link-local, shared, documentation,
              multicast and reserved addresses, and internal hostnames are rejected, as are
              credentials embedded in the URL or in credential-looking query parameters. At
              most 2048 characters.

          connect_timeout_ms: How long Telnyx waits for the WebSocket connection to open, from 500 to 10000.
              Default: 3000.

          contact_email: A contact address stored for the Telnyx platform team. Telnyx does not email it
              automatically. At most 254 characters.

          data_retention_policy_url: URL of the publisher's data retention policy, at most 2048 characters. It is
              returned in the discoverable listing.

          documentation_url: An `https://` page where callers learn how to get a key for the engine and how
              to use it, with a host and no credentials in it, at most 2048 characters. It is
              returned in the discoverable listing.

          visibility: `private`: only your organization can use the engine. `public`: any organization
              can, once it is `active`.

          voices_api_key_ref: The identifier of an Integration Secret in your organization. When set, Telnyx
              sends its value as a bearer token when it reads `voices_url`. It is never used
              for synthesis. Send `null` on an update to clear it. At most 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tts_integrations",
            body=await async_maybe_transform(
                {
                    "capabilities": capabilities,
                    "name": name,
                    "supported_audio_formats": supported_audio_formats,
                    "voices_url": voices_url,
                    "websocket_url": websocket_url,
                    "connect_timeout_ms": connect_timeout_ms,
                    "contact_email": contact_email,
                    "data_retention_policy_url": data_retention_policy_url,
                    "documentation_url": documentation_url,
                    "visibility": visibility,
                    "voices_api_key_ref": voices_api_key_ref,
                },
                tts_integration_create_params.TtsIntegrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsEngine:
        """
        Retrieve one of your own community TTS engines by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/tts_integrations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    async def update(
        self,
        id: str,
        *,
        capabilities: CommunityTtsEngineCapabilitiesParam | Omit = omit,
        connect_timeout_ms: int | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        data_retention_policy_url: Optional[str] | Omit = omit,
        documentation_url: Optional[str] | Omit = omit,
        supported_audio_formats: List[CommunityTtsAudioFormat] | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        voices_api_key_ref: Optional[str] | Omit = omit,
        voices_url: str | Omit = omit,
        websocket_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsEngine:
        """
        Same as `PUT`: only the fields you send change.

        Args:
          capabilities: What the engine supports. An unknown key is rejected.

          visibility: `private`: only your organization can use the engine. `public`: any organization
              can, once it is `active`.

          voices_url: See the create request.

          websocket_url: See the create request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/tts_integrations/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "capabilities": capabilities,
                    "connect_timeout_ms": connect_timeout_ms,
                    "contact_email": contact_email,
                    "data_retention_policy_url": data_retention_policy_url,
                    "documentation_url": documentation_url,
                    "supported_audio_formats": supported_audio_formats,
                    "visibility": visibility,
                    "voices_api_key_ref": voices_api_key_ref,
                    "voices_url": voices_url,
                    "websocket_url": websocket_url,
                },
                tts_integration_update_params.TtsIntegrationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    async def list(
        self,
        *,
        page: tts_integration_list_params.Page | Omit = omit,
        status: CommunityTtsEngineStatus | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TtsIntegrationListResponse:
        """
        List every community TTS engine your organization has registered, at any status
        or visibility. Use `GET /tts_integrations/discoverable` instead to also see
        other organizations' public, active engines.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          status: Filter by status.

          visibility: Filter by visibility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/tts_integrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "status": status,
                        "visibility": visibility,
                    },
                    tts_integration_list_params.TtsIntegrationListParams,
                ),
            ),
            cast_to=TtsIntegrationListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete one of your own community TTS engines.

        The engine disappears from every
        listing and lookup and can no longer serve traffic, but its `name` stays
        reserved for your organization: no other organization can register it, and you
        can register it again later. An assistant or call still configured with one of
        its voices cannot use it until an engine with that name exists again.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/tts_integrations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def replace(
        self,
        id: str,
        *,
        capabilities: CommunityTtsEngineCapabilitiesParam | Omit = omit,
        connect_timeout_ms: int | Omit = omit,
        contact_email: Optional[str] | Omit = omit,
        data_retention_policy_url: Optional[str] | Omit = omit,
        documentation_url: Optional[str] | Omit = omit,
        supported_audio_formats: List[CommunityTtsAudioFormat] | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        voices_api_key_ref: Optional[str] | Omit = omit,
        voices_url: str | Omit = omit,
        websocket_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsEngine:
        """Change one of your own community TTS engines.

        Every field is optional: omit a
        field to leave it unchanged. `name` cannot be changed. Telnyx reads the
        `voices_url` again and refuses an update that leaves the engine with an
        unreadable list. Changing `websocket_url`, `voices_url`,
        `supported_audio_formats` or `capabilities`, or making a `private` engine
        `public`, sends the engine back to `status: draft` and clears its review. See
        the [Community TTS engines guide](/docs/voice/tts/community-engines) for the
        full review flow.

        Args:
          capabilities: What the engine supports. An unknown key is rejected.

          visibility: `private`: only your organization can use the engine. `public`: any organization
              can, once it is `active`.

          voices_url: See the create request.

          websocket_url: See the create request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            path_template("/tts_integrations/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "capabilities": capabilities,
                    "connect_timeout_ms": connect_timeout_ms,
                    "contact_email": contact_email,
                    "data_retention_policy_url": data_retention_policy_url,
                    "documentation_url": documentation_url,
                    "supported_audio_formats": supported_audio_formats,
                    "visibility": visibility,
                    "voices_api_key_ref": voices_api_key_ref,
                    "voices_url": voices_url,
                    "websocket_url": websocket_url,
                },
                tts_integration_replace_params.TtsIntegrationReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    async def retrieve_conformance_runs(
        self,
        id: str,
        *,
        page: tts_integration_retrieve_conformance_runs_params.Page | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TtsIntegrationRetrieveConformanceRunsResponse:
        """
        The recorded runs of `test_connection` for one of your engines, newest first.
        Telnyx keeps the latest 50.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/tts_integrations/{id}/conformance_runs", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"page": page},
                    tts_integration_retrieve_conformance_runs_params.TtsIntegrationRetrieveConformanceRunsParams,
                ),
            ),
            cast_to=TtsIntegrationRetrieveConformanceRunsResponse,
        )

    async def retrieve_discoverable(
        self,
        *,
        page: tts_integration_retrieve_discoverable_params.Page | Omit = omit,
        status: CommunityTtsEngineStatus | Omit = omit,
        visibility: CommunityTtsEngineVisibility | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TtsIntegrationRetrieveDiscoverableResponse:
        """
        List the engines you can use: your own, at any status, and other organizations'
        engines that are `public` and `active`. Each entry carries what a caller needs
        to choose an engine: its `name` (the first part of its voices,
        `<name>.<voice_id>`), `voices_count`, audio formats, capabilities, and
        `documentation_url`. It never carries the publisher's contact details, review
        notes, or `voices_api_key_ref`. Read an engine's voices with
        `GET /tts_integrations/{id}/voices`.

        Args:
          page: Consolidated page parameter (deepObject style). Originally: page[size],
              page[number]

          status: Filter by status.

          visibility: Filter by visibility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/tts_integrations/discoverable",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "status": status,
                        "visibility": visibility,
                    },
                    tts_integration_retrieve_discoverable_params.TtsIntegrationRetrieveDiscoverableParams,
                ),
            ),
            cast_to=TtsIntegrationRetrieveDiscoverableResponse,
        )

    async def retrieve_voices(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TtsIntegrationRetrieveVoicesResponse:
        """
        The voices Telnyx last read from the engine's `voices_url`, in the shape the
        engine published. A caller selects one as `<engine name>.<voice_id>`. The list
        is replaced only when a new read succeeds, so an engine whose `voices_url` is
        down keeps serving its last list. `[]` until the first read succeeds.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/tts_integrations/{id}/voices", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TtsIntegrationRetrieveVoicesResponse,
        )


class TtsIntegrationsResourceWithRawResponse:
    def __init__(self, tts_integrations: TtsIntegrationsResource) -> None:
        self._tts_integrations = tts_integrations

        self.create = to_raw_response_wrapper(
            tts_integrations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tts_integrations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tts_integrations.update,
        )
        self.list = to_raw_response_wrapper(
            tts_integrations.list,
        )
        self.delete = to_raw_response_wrapper(
            tts_integrations.delete,
        )
        self.replace = to_raw_response_wrapper(
            tts_integrations.replace,
        )
        self.retrieve_conformance_runs = to_raw_response_wrapper(
            tts_integrations.retrieve_conformance_runs,
        )
        self.retrieve_discoverable = to_raw_response_wrapper(
            tts_integrations.retrieve_discoverable,
        )
        self.retrieve_voices = to_raw_response_wrapper(
            tts_integrations.retrieve_voices,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        """
        Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
        """
        return ActionsResourceWithRawResponse(self._tts_integrations.actions)


class AsyncTtsIntegrationsResourceWithRawResponse:
    def __init__(self, tts_integrations: AsyncTtsIntegrationsResource) -> None:
        self._tts_integrations = tts_integrations

        self.create = async_to_raw_response_wrapper(
            tts_integrations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tts_integrations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tts_integrations.update,
        )
        self.list = async_to_raw_response_wrapper(
            tts_integrations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tts_integrations.delete,
        )
        self.replace = async_to_raw_response_wrapper(
            tts_integrations.replace,
        )
        self.retrieve_conformance_runs = async_to_raw_response_wrapper(
            tts_integrations.retrieve_conformance_runs,
        )
        self.retrieve_discoverable = async_to_raw_response_wrapper(
            tts_integrations.retrieve_discoverable,
        )
        self.retrieve_voices = async_to_raw_response_wrapper(
            tts_integrations.retrieve_voices,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        """
        Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
        """
        return AsyncActionsResourceWithRawResponse(self._tts_integrations.actions)


class TtsIntegrationsResourceWithStreamingResponse:
    def __init__(self, tts_integrations: TtsIntegrationsResource) -> None:
        self._tts_integrations = tts_integrations

        self.create = to_streamed_response_wrapper(
            tts_integrations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tts_integrations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tts_integrations.update,
        )
        self.list = to_streamed_response_wrapper(
            tts_integrations.list,
        )
        self.delete = to_streamed_response_wrapper(
            tts_integrations.delete,
        )
        self.replace = to_streamed_response_wrapper(
            tts_integrations.replace,
        )
        self.retrieve_conformance_runs = to_streamed_response_wrapper(
            tts_integrations.retrieve_conformance_runs,
        )
        self.retrieve_discoverable = to_streamed_response_wrapper(
            tts_integrations.retrieve_discoverable,
        )
        self.retrieve_voices = to_streamed_response_wrapper(
            tts_integrations.retrieve_voices,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        """
        Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
        """
        return ActionsResourceWithStreamingResponse(self._tts_integrations.actions)


class AsyncTtsIntegrationsResourceWithStreamingResponse:
    def __init__(self, tts_integrations: AsyncTtsIntegrationsResource) -> None:
        self._tts_integrations = tts_integrations

        self.create = async_to_streamed_response_wrapper(
            tts_integrations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tts_integrations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tts_integrations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tts_integrations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tts_integrations.delete,
        )
        self.replace = async_to_streamed_response_wrapper(
            tts_integrations.replace,
        )
        self.retrieve_conformance_runs = async_to_streamed_response_wrapper(
            tts_integrations.retrieve_conformance_runs,
        )
        self.retrieve_discoverable = async_to_streamed_response_wrapper(
            tts_integrations.retrieve_discoverable,
        )
        self.retrieve_voices = async_to_streamed_response_wrapper(
            tts_integrations.retrieve_voices,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
        """
        return AsyncActionsResourceWithStreamingResponse(self._tts_integrations.actions)
