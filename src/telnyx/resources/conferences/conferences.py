# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...types import (
    conference_list_params,
    conference_create_params,
    conference_retrieve_params,
    conference_list_participants_params,
)
from .actions import (
    ActionsResource,
    AsyncActionsResource,
    ActionsResourceWithRawResponse,
    AsyncActionsResourceWithRawResponse,
    ActionsResourceWithStreamingResponse,
    AsyncActionsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.conference import Conference
from ...types.conference_create_response import ConferenceCreateResponse
from ...types.conference_retrieve_response import ConferenceRetrieveResponse
from ...types.conference_list_participants_response import ConferenceListParticipantsResponse

__all__ = ["ConferencesResource", "AsyncConferencesResource"]


class ConferencesResource(SyncAPIResource):
    @cached_property
    def actions(self) -> ActionsResource:
        return ActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ConferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ConferencesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        call_control_id: str,
        name: str,
        beep_enabled: Literal["always", "never", "on_enter", "on_exit"] | Omit = omit,
        client_state: str | Omit = omit,
        comfort_noise: bool | Omit = omit,
        command_id: str | Omit = omit,
        duration_minutes: int | Omit = omit,
        hold_audio_url: str | Omit = omit,
        hold_media_name: str | Omit = omit,
        max_participants: int | Omit = omit,
        region: Literal["Australia", "Europe", "Middle East", "US"] | Omit = omit,
        start_conference_on_create: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConferenceCreateResponse:
        """
        Create a conference from an existing call leg using a `call_control_id` and a
        conference name. Upon creating the conference, the call will be automatically
        bridged to the conference. Conferences will expire after all participants have
        left the conference or after 4 hours regardless of the number of active
        participants.

        **Expected Webhooks:**

        - `conference.created`
        - `conference.participant.joined`
        - `conference.participant.left`
        - `conference.ended`
        - `conference.recording.saved`
        - `conference.floor.changed`

        Args:
          call_control_id: Unique identifier and token for controlling the call

          name: Name of the conference

          beep_enabled: Whether a beep sound should be played when participants join and/or leave the
              conference.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string. The client_state will be updated for the creator call
              leg and will be used for all webhooks related to the created conference.

          comfort_noise: Toggle background comfort noise.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          duration_minutes: Time length (minutes) after which the conference will end.

          hold_audio_url: The URL of a file to be played to participants joining the conference. The URL
              can point to either a WAV or MP3 file. hold_media_name and hold_audio_url cannot
              be used together in one request. Takes effect only when
              "start_conference_on_create" is set to "false".

          hold_media_name: The media_name of a file to be played to participants joining the conference.
              The media_name must point to a file previously uploaded to
              api.telnyx.com/v2/media by the same user/organization. The file must either be a
              WAV or MP3 file. Takes effect only when "start_conference_on_create" is set to
              "false".

          max_participants: The maximum number of active conference participants to allow. Must be between 2
              and 800. Defaults to 250

          region: Sets the region where the conference data will be hosted. Defaults to the region
              defined in user's data locality settings (Europe or US).

          start_conference_on_create: Whether the conference should be started on creation. If the conference isn't
              started all participants that join are automatically put on hold. Defaults to
              "true".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/conferences",
            body=maybe_transform(
                {
                    "call_control_id": call_control_id,
                    "name": name,
                    "beep_enabled": beep_enabled,
                    "client_state": client_state,
                    "comfort_noise": comfort_noise,
                    "command_id": command_id,
                    "duration_minutes": duration_minutes,
                    "hold_audio_url": hold_audio_url,
                    "hold_media_name": hold_media_name,
                    "max_participants": max_participants,
                    "region": region,
                    "start_conference_on_create": start_conference_on_create,
                },
                conference_create_params.ConferenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        region: Literal["Australia", "Europe", "Middle East", "US"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConferenceRetrieveResponse:
        """
        Retrieve an existing conference

        Args:
          region: Region where the conference data is located

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/conferences/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"region": region}, conference_retrieve_params.ConferenceRetrieveParams),
            ),
            cast_to=ConferenceRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: conference_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        region: Literal["Australia", "Europe", "Middle East", "US"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[Conference]:
        """Lists conferences.

        Conferences are created on demand, and will expire after all
        participants have left the conference or after 4 hours regardless of the number
        of active participants. Conferences are listed in descending order by
        `expires_at`.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[application_name][contains], filter[outbound.outbound_voice_profile_id],
              filter[leg_id], filter[application_session_id], filter[connection_id],
              filter[product], filter[failed], filter[from], filter[to], filter[name],
              filter[type], filter[occurred_at][eq/gt/gte/lt/lte], filter[status]

          region: Region where the conference data is located

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conferences",
            page=SyncDefaultFlatPagination[Conference],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "region": region,
                    },
                    conference_list_params.ConferenceListParams,
                ),
            ),
            model=Conference,
        )

    def list_participants(
        self,
        conference_id: str,
        *,
        filter: conference_list_participants_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        region: Literal["Australia", "Europe", "Middle East", "US"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[ConferenceListParticipantsResponse]:
        """
        Lists conference participants

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[muted],
              filter[on_hold], filter[whispering]

          region: Region where the conference data is located

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conference_id:
            raise ValueError(f"Expected a non-empty value for `conference_id` but received {conference_id!r}")
        return self._get_api_list(
            f"/conferences/{conference_id}/participants",
            page=SyncDefaultFlatPagination[ConferenceListParticipantsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "region": region,
                    },
                    conference_list_participants_params.ConferenceListParticipantsParams,
                ),
            ),
            model=ConferenceListParticipantsResponse,
        )


class AsyncConferencesResource(AsyncAPIResource):
    @cached_property
    def actions(self) -> AsyncActionsResource:
        return AsyncActionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncConferencesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        call_control_id: str,
        name: str,
        beep_enabled: Literal["always", "never", "on_enter", "on_exit"] | Omit = omit,
        client_state: str | Omit = omit,
        comfort_noise: bool | Omit = omit,
        command_id: str | Omit = omit,
        duration_minutes: int | Omit = omit,
        hold_audio_url: str | Omit = omit,
        hold_media_name: str | Omit = omit,
        max_participants: int | Omit = omit,
        region: Literal["Australia", "Europe", "Middle East", "US"] | Omit = omit,
        start_conference_on_create: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConferenceCreateResponse:
        """
        Create a conference from an existing call leg using a `call_control_id` and a
        conference name. Upon creating the conference, the call will be automatically
        bridged to the conference. Conferences will expire after all participants have
        left the conference or after 4 hours regardless of the number of active
        participants.

        **Expected Webhooks:**

        - `conference.created`
        - `conference.participant.joined`
        - `conference.participant.left`
        - `conference.ended`
        - `conference.recording.saved`
        - `conference.floor.changed`

        Args:
          call_control_id: Unique identifier and token for controlling the call

          name: Name of the conference

          beep_enabled: Whether a beep sound should be played when participants join and/or leave the
              conference.

          client_state: Use this field to add state to every subsequent webhook. It must be a valid
              Base-64 encoded string. The client_state will be updated for the creator call
              leg and will be used for all webhooks related to the created conference.

          comfort_noise: Toggle background comfort noise.

          command_id: Use this field to avoid execution of duplicate commands. Telnyx will ignore
              subsequent commands with the same `command_id` as one that has already been
              executed.

          duration_minutes: Time length (minutes) after which the conference will end.

          hold_audio_url: The URL of a file to be played to participants joining the conference. The URL
              can point to either a WAV or MP3 file. hold_media_name and hold_audio_url cannot
              be used together in one request. Takes effect only when
              "start_conference_on_create" is set to "false".

          hold_media_name: The media_name of a file to be played to participants joining the conference.
              The media_name must point to a file previously uploaded to
              api.telnyx.com/v2/media by the same user/organization. The file must either be a
              WAV or MP3 file. Takes effect only when "start_conference_on_create" is set to
              "false".

          max_participants: The maximum number of active conference participants to allow. Must be between 2
              and 800. Defaults to 250

          region: Sets the region where the conference data will be hosted. Defaults to the region
              defined in user's data locality settings (Europe or US).

          start_conference_on_create: Whether the conference should be started on creation. If the conference isn't
              started all participants that join are automatically put on hold. Defaults to
              "true".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/conferences",
            body=await async_maybe_transform(
                {
                    "call_control_id": call_control_id,
                    "name": name,
                    "beep_enabled": beep_enabled,
                    "client_state": client_state,
                    "comfort_noise": comfort_noise,
                    "command_id": command_id,
                    "duration_minutes": duration_minutes,
                    "hold_audio_url": hold_audio_url,
                    "hold_media_name": hold_media_name,
                    "max_participants": max_participants,
                    "region": region,
                    "start_conference_on_create": start_conference_on_create,
                },
                conference_create_params.ConferenceCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        region: Literal["Australia", "Europe", "Middle East", "US"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConferenceRetrieveResponse:
        """
        Retrieve an existing conference

        Args:
          region: Region where the conference data is located

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/conferences/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"region": region}, conference_retrieve_params.ConferenceRetrieveParams
                ),
            ),
            cast_to=ConferenceRetrieveResponse,
        )

    def list(
        self,
        *,
        filter: conference_list_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        region: Literal["Australia", "Europe", "Middle East", "US"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Conference, AsyncDefaultFlatPagination[Conference]]:
        """Lists conferences.

        Conferences are created on demand, and will expire after all
        participants have left the conference or after 4 hours regardless of the number
        of active participants. Conferences are listed in descending order by
        `expires_at`.

        Args:
          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[application_name][contains], filter[outbound.outbound_voice_profile_id],
              filter[leg_id], filter[application_session_id], filter[connection_id],
              filter[product], filter[failed], filter[from], filter[to], filter[name],
              filter[type], filter[occurred_at][eq/gt/gte/lt/lte], filter[status]

          region: Region where the conference data is located

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/conferences",
            page=AsyncDefaultFlatPagination[Conference],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "region": region,
                    },
                    conference_list_params.ConferenceListParams,
                ),
            ),
            model=Conference,
        )

    def list_participants(
        self,
        conference_id: str,
        *,
        filter: conference_list_participants_params.Filter | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        region: Literal["Australia", "Europe", "Middle East", "US"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[
        ConferenceListParticipantsResponse, AsyncDefaultFlatPagination[ConferenceListParticipantsResponse]
    ]:
        """
        Lists conference participants

        Args:
          filter: Consolidated filter parameter (deepObject style). Originally: filter[muted],
              filter[on_hold], filter[whispering]

          region: Region where the conference data is located

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not conference_id:
            raise ValueError(f"Expected a non-empty value for `conference_id` but received {conference_id!r}")
        return self._get_api_list(
            f"/conferences/{conference_id}/participants",
            page=AsyncDefaultFlatPagination[ConferenceListParticipantsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page_number": page_number,
                        "page_size": page_size,
                        "region": region,
                    },
                    conference_list_participants_params.ConferenceListParticipantsParams,
                ),
            ),
            model=ConferenceListParticipantsResponse,
        )


class ConferencesResourceWithRawResponse:
    def __init__(self, conferences: ConferencesResource) -> None:
        self._conferences = conferences

        self.create = to_raw_response_wrapper(
            conferences.create,
        )
        self.retrieve = to_raw_response_wrapper(
            conferences.retrieve,
        )
        self.list = to_raw_response_wrapper(
            conferences.list,
        )
        self.list_participants = to_raw_response_wrapper(
            conferences.list_participants,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithRawResponse:
        return ActionsResourceWithRawResponse(self._conferences.actions)


class AsyncConferencesResourceWithRawResponse:
    def __init__(self, conferences: AsyncConferencesResource) -> None:
        self._conferences = conferences

        self.create = async_to_raw_response_wrapper(
            conferences.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            conferences.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            conferences.list,
        )
        self.list_participants = async_to_raw_response_wrapper(
            conferences.list_participants,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithRawResponse:
        return AsyncActionsResourceWithRawResponse(self._conferences.actions)


class ConferencesResourceWithStreamingResponse:
    def __init__(self, conferences: ConferencesResource) -> None:
        self._conferences = conferences

        self.create = to_streamed_response_wrapper(
            conferences.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            conferences.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            conferences.list,
        )
        self.list_participants = to_streamed_response_wrapper(
            conferences.list_participants,
        )

    @cached_property
    def actions(self) -> ActionsResourceWithStreamingResponse:
        return ActionsResourceWithStreamingResponse(self._conferences.actions)


class AsyncConferencesResourceWithStreamingResponse:
    def __init__(self, conferences: AsyncConferencesResource) -> None:
        self._conferences = conferences

        self.create = async_to_streamed_response_wrapper(
            conferences.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            conferences.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            conferences.list,
        )
        self.list_participants = async_to_streamed_response_wrapper(
            conferences.list_participants,
        )

    @cached_property
    def actions(self) -> AsyncActionsResourceWithStreamingResponse:
        return AsyncActionsResourceWithStreamingResponse(self._conferences.actions)
