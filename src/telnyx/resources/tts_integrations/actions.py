# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.tts_integrations import action_test_connection_params
from ...types.community_tts_engine import CommunityTtsEngine
from ...types.tts_integrations.community_tts_conformance_run import CommunityTtsConformanceRun

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    """
    Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
    """

    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def disable(
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
        Pause an `active` engine so it stops serving traffic, without deleting it.
        Owner-initiated and owner-reversible via `enable`. Only an `active` engine can
        be disabled. While an engine is disabled, no organization can use it, including
        other organizations if it is `public`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/tts_integrations/{id}/actions/disable", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    def enable(
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
        """Resume a `disabled` engine.

        Only a `disabled` engine can be enabled; a
        `suspended` engine can only be reinstated by Telnyx.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/tts_integrations/{id}/actions/enable", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    def refresh_voices(
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
        Make Telnyx read the engine's `voices_url` now instead of at the next scheduled
        read (every 15 minutes). On success the stored list is replaced and
        `voices_degraded` is cleared. The previous list is kept when the read fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/tts_integrations/{id}/actions/refresh_voices", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    def request_review(
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
        """Ask Telnyx to review a `draft` engine so it can serve other organizations.

        Only
        a `draft` engine with no pending or approved review can be submitted (a rejected
        one can be submitted again). The engine moves to `review_status: pending`;
        Telnyx approves it (`status: active`, `review_status: approved`) or rejects it
        with `review_notes`. See the
        [Community TTS engines guide](/docs/voice/tts/community-engines) for the full
        review flow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/tts_integrations/{id}/actions/request_review", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    def test_connection(
        self,
        id: str,
        *,
        api_key_ref: str,
        voice_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsConformanceRun:
        """Check an engine end to end with your own key, without a call.

        Telnyx reads the
        voice list, connects to the engine's `websocket_url` with the Integration Secret
        named by `api_key_ref`, sends a short text, and checks the answer: the
        handshake, the credentials, the audio, the final frame and a clean close. The
        result is recorded (see `conformance_runs`) and returned. A test within 10
        seconds of the previous one is refused with `429`, and a `suspended` engine
        cannot be tested. See
        [Try your engine before approval](/docs/voice/tts/community-engines#try-your-engine-before-approval).

        Args:
          api_key_ref: The identifier of the Integration Secret in your organization that Telnyx
              connects to the engine with, as a caller would.

          voice_id: The voice to test. Default: the first voice in the engine's list. It must be in
              the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/tts_integrations/{id}/actions/test_connection", id=id),
            body=maybe_transform(
                {
                    "api_key_ref": api_key_ref,
                    "voice_id": voice_id,
                },
                action_test_connection_params.ActionTestConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsConformanceRun,
        )


class AsyncActionsResource(AsyncAPIResource):
    """
    Register and manage text-to-speech (TTS) engines you publish, and find the public engines other organizations published, so an AI Assistant, TeXML or Call Control can speak with one of their voices, using your own key for it, instead of a Telnyx-integrated vendor.
    """

    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def disable(
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
        Pause an `active` engine so it stops serving traffic, without deleting it.
        Owner-initiated and owner-reversible via `enable`. Only an `active` engine can
        be disabled. While an engine is disabled, no organization can use it, including
        other organizations if it is `public`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/tts_integrations/{id}/actions/disable", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    async def enable(
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
        """Resume a `disabled` engine.

        Only a `disabled` engine can be enabled; a
        `suspended` engine can only be reinstated by Telnyx.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/tts_integrations/{id}/actions/enable", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    async def refresh_voices(
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
        Make Telnyx read the engine's `voices_url` now instead of at the next scheduled
        read (every 15 minutes). On success the stored list is replaced and
        `voices_degraded` is cleared. The previous list is kept when the read fails.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/tts_integrations/{id}/actions/refresh_voices", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    async def request_review(
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
        """Ask Telnyx to review a `draft` engine so it can serve other organizations.

        Only
        a `draft` engine with no pending or approved review can be submitted (a rejected
        one can be submitted again). The engine moves to `review_status: pending`;
        Telnyx approves it (`status: active`, `review_status: approved`) or rejects it
        with `review_notes`. See the
        [Community TTS engines guide](/docs/voice/tts/community-engines) for the full
        review flow.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/tts_integrations/{id}/actions/request_review", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsEngine,
        )

    async def test_connection(
        self,
        id: str,
        *,
        api_key_ref: str,
        voice_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CommunityTtsConformanceRun:
        """Check an engine end to end with your own key, without a call.

        Telnyx reads the
        voice list, connects to the engine's `websocket_url` with the Integration Secret
        named by `api_key_ref`, sends a short text, and checks the answer: the
        handshake, the credentials, the audio, the final frame and a clean close. The
        result is recorded (see `conformance_runs`) and returned. A test within 10
        seconds of the previous one is refused with `429`, and a `suspended` engine
        cannot be tested. See
        [Try your engine before approval](/docs/voice/tts/community-engines#try-your-engine-before-approval).

        Args:
          api_key_ref: The identifier of the Integration Secret in your organization that Telnyx
              connects to the engine with, as a caller would.

          voice_id: The voice to test. Default: the first voice in the engine's list. It must be in
              the list.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/tts_integrations/{id}/actions/test_connection", id=id),
            body=await async_maybe_transform(
                {
                    "api_key_ref": api_key_ref,
                    "voice_id": voice_id,
                },
                action_test_connection_params.ActionTestConnectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CommunityTtsConformanceRun,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.disable = to_raw_response_wrapper(
            actions.disable,
        )
        self.enable = to_raw_response_wrapper(
            actions.enable,
        )
        self.refresh_voices = to_raw_response_wrapper(
            actions.refresh_voices,
        )
        self.request_review = to_raw_response_wrapper(
            actions.request_review,
        )
        self.test_connection = to_raw_response_wrapper(
            actions.test_connection,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.disable = async_to_raw_response_wrapper(
            actions.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            actions.enable,
        )
        self.refresh_voices = async_to_raw_response_wrapper(
            actions.refresh_voices,
        )
        self.request_review = async_to_raw_response_wrapper(
            actions.request_review,
        )
        self.test_connection = async_to_raw_response_wrapper(
            actions.test_connection,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.disable = to_streamed_response_wrapper(
            actions.disable,
        )
        self.enable = to_streamed_response_wrapper(
            actions.enable,
        )
        self.refresh_voices = to_streamed_response_wrapper(
            actions.refresh_voices,
        )
        self.request_review = to_streamed_response_wrapper(
            actions.request_review,
        )
        self.test_connection = to_streamed_response_wrapper(
            actions.test_connection,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.disable = async_to_streamed_response_wrapper(
            actions.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            actions.enable,
        )
        self.refresh_voices = async_to_streamed_response_wrapper(
            actions.refresh_voices,
        )
        self.request_review = async_to_streamed_response_wrapper(
            actions.request_review,
        )
        self.test_connection = async_to_streamed_response_wrapper(
            actions.test_connection,
        )
