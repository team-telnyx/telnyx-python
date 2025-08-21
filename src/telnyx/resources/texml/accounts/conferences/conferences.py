# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from .participants import (
    ParticipantsResource,
    AsyncParticipantsResource,
    ParticipantsResourceWithRawResponse,
    AsyncParticipantsResourceWithRawResponse,
    ParticipantsResourceWithStreamingResponse,
    AsyncParticipantsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.texml.accounts import conference_update_params, conference_retrieve_conferences_params
from .....types.texml.accounts.conference_update_response import ConferenceUpdateResponse
from .....types.texml.accounts.conference_retrieve_response import ConferenceRetrieveResponse
from .....types.texml.accounts.conference_retrieve_recordings_response import ConferenceRetrieveRecordingsResponse
from .....types.texml.accounts.conference_retrieve_conferences_response import ConferenceRetrieveConferencesResponse
from .....types.texml.accounts.conference_retrieve_recordings_json_response import (
    ConferenceRetrieveRecordingsJsonResponse,
)

__all__ = ["ConferencesResource", "AsyncConferencesResource"]


class ConferencesResource(SyncAPIResource):
    @cached_property
    def participants(self) -> ParticipantsResource:
        return ParticipantsResource(self._client)

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

    def retrieve(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceRetrieveResponse:
        """
        Returns a conference resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceRetrieveResponse,
        )

    def update(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        announce_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        announce_url: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceUpdateResponse:
        """
        Updates a conference resource.

        Args:
          announce_method: The HTTP method used to call the `AnnounceUrl`. Defaults to `POST`.

          announce_url: The URL we should call to announce something into the conference. The URL may
              return an MP3 file, a WAV file, or a TwiML document that contains `<Play>`,
              `<Say>`, `<Pause>`, or `<Redirect>` verbs.

          status: The new status of the resource. Specifying `completed` will end the conference
              and hang up all participants.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return self._post(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}",
            body=maybe_transform(
                {
                    "announce_method": announce_method,
                    "announce_url": announce_url,
                    "status": status,
                },
                conference_update_params.ConferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceUpdateResponse,
        )

    def retrieve_conferences(
        self,
        account_sid: str,
        *,
        date_created: str | NotGiven = NOT_GIVEN,
        date_updated: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        status: Literal["init", "in-progress", "completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceRetrieveConferencesResponse:
        """
        Lists conference resources.

        Args:
          date_created: Filters conferences by the creation date. Expected format is YYYY-MM-DD. Also
              accepts inequality operators, e.g. DateCreated>=2023-05-22.

          date_updated: Filters conferences by the time they were last updated. Expected format is
              YYYY-MM-DD. Also accepts inequality operators, e.g. DateUpdated>=2023-05-22.

          friendly_name: Filters conferences by their friendly name.

          page: The number of the page to be displayed, zero-indexed, should be used in
              conjuction with PageToken.

          page_size: The number of records to be displayed on a page

          page_token: Used to request the next page of results.

          status: Filters conferences by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Conferences",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_created": date_created,
                        "date_updated": date_updated,
                        "friendly_name": friendly_name,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                        "status": status,
                    },
                    conference_retrieve_conferences_params.ConferenceRetrieveConferencesParams,
                ),
            ),
            cast_to=ConferenceRetrieveConferencesResponse,
        )

    def retrieve_recordings(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceRetrieveRecordingsResponse:
        """
        Lists conference recordings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceRetrieveRecordingsResponse,
        )

    def retrieve_recordings_json(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceRetrieveRecordingsJsonResponse:
        """
        Returns recordings for a conference identified by conference_sid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceRetrieveRecordingsJsonResponse,
        )


class AsyncConferencesResource(AsyncAPIResource):
    @cached_property
    def participants(self) -> AsyncParticipantsResource:
        return AsyncParticipantsResource(self._client)

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

    async def retrieve(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceRetrieveResponse:
        """
        Returns a conference resource.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceRetrieveResponse,
        )

    async def update(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        announce_method: Literal["GET", "POST"] | NotGiven = NOT_GIVEN,
        announce_url: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceUpdateResponse:
        """
        Updates a conference resource.

        Args:
          announce_method: The HTTP method used to call the `AnnounceUrl`. Defaults to `POST`.

          announce_url: The URL we should call to announce something into the conference. The URL may
              return an MP3 file, a WAV file, or a TwiML document that contains `<Play>`,
              `<Say>`, `<Pause>`, or `<Redirect>` verbs.

          status: The new status of the resource. Specifying `completed` will end the conference
              and hang up all participants.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return await self._post(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}",
            body=await async_maybe_transform(
                {
                    "announce_method": announce_method,
                    "announce_url": announce_url,
                    "status": status,
                },
                conference_update_params.ConferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceUpdateResponse,
        )

    async def retrieve_conferences(
        self,
        account_sid: str,
        *,
        date_created: str | NotGiven = NOT_GIVEN,
        date_updated: str | NotGiven = NOT_GIVEN,
        friendly_name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        status: Literal["init", "in-progress", "completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceRetrieveConferencesResponse:
        """
        Lists conference resources.

        Args:
          date_created: Filters conferences by the creation date. Expected format is YYYY-MM-DD. Also
              accepts inequality operators, e.g. DateCreated>=2023-05-22.

          date_updated: Filters conferences by the time they were last updated. Expected format is
              YYYY-MM-DD. Also accepts inequality operators, e.g. DateUpdated>=2023-05-22.

          friendly_name: Filters conferences by their friendly name.

          page: The number of the page to be displayed, zero-indexed, should be used in
              conjuction with PageToken.

          page_size: The number of records to be displayed on a page

          page_token: Used to request the next page of results.

          status: Filters conferences by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Conferences",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_created": date_created,
                        "date_updated": date_updated,
                        "friendly_name": friendly_name,
                        "page": page,
                        "page_size": page_size,
                        "page_token": page_token,
                        "status": status,
                    },
                    conference_retrieve_conferences_params.ConferenceRetrieveConferencesParams,
                ),
            ),
            cast_to=ConferenceRetrieveConferencesResponse,
        )

    async def retrieve_recordings(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceRetrieveRecordingsResponse:
        """
        Lists conference recordings

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceRetrieveRecordingsResponse,
        )

    async def retrieve_recordings_json(
        self,
        conference_sid: str,
        *,
        account_sid: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConferenceRetrieveRecordingsJsonResponse:
        """
        Returns recordings for a conference identified by conference_sid.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        if not conference_sid:
            raise ValueError(f"Expected a non-empty value for `conference_sid` but received {conference_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Conferences/{conference_sid}/Recordings.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConferenceRetrieveRecordingsJsonResponse,
        )


class ConferencesResourceWithRawResponse:
    def __init__(self, conferences: ConferencesResource) -> None:
        self._conferences = conferences

        self.retrieve = to_raw_response_wrapper(
            conferences.retrieve,
        )
        self.update = to_raw_response_wrapper(
            conferences.update,
        )
        self.retrieve_conferences = to_raw_response_wrapper(
            conferences.retrieve_conferences,
        )
        self.retrieve_recordings = to_raw_response_wrapper(
            conferences.retrieve_recordings,
        )
        self.retrieve_recordings_json = to_raw_response_wrapper(
            conferences.retrieve_recordings_json,
        )

    @cached_property
    def participants(self) -> ParticipantsResourceWithRawResponse:
        return ParticipantsResourceWithRawResponse(self._conferences.participants)


class AsyncConferencesResourceWithRawResponse:
    def __init__(self, conferences: AsyncConferencesResource) -> None:
        self._conferences = conferences

        self.retrieve = async_to_raw_response_wrapper(
            conferences.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            conferences.update,
        )
        self.retrieve_conferences = async_to_raw_response_wrapper(
            conferences.retrieve_conferences,
        )
        self.retrieve_recordings = async_to_raw_response_wrapper(
            conferences.retrieve_recordings,
        )
        self.retrieve_recordings_json = async_to_raw_response_wrapper(
            conferences.retrieve_recordings_json,
        )

    @cached_property
    def participants(self) -> AsyncParticipantsResourceWithRawResponse:
        return AsyncParticipantsResourceWithRawResponse(self._conferences.participants)


class ConferencesResourceWithStreamingResponse:
    def __init__(self, conferences: ConferencesResource) -> None:
        self._conferences = conferences

        self.retrieve = to_streamed_response_wrapper(
            conferences.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            conferences.update,
        )
        self.retrieve_conferences = to_streamed_response_wrapper(
            conferences.retrieve_conferences,
        )
        self.retrieve_recordings = to_streamed_response_wrapper(
            conferences.retrieve_recordings,
        )
        self.retrieve_recordings_json = to_streamed_response_wrapper(
            conferences.retrieve_recordings_json,
        )

    @cached_property
    def participants(self) -> ParticipantsResourceWithStreamingResponse:
        return ParticipantsResourceWithStreamingResponse(self._conferences.participants)


class AsyncConferencesResourceWithStreamingResponse:
    def __init__(self, conferences: AsyncConferencesResource) -> None:
        self._conferences = conferences

        self.retrieve = async_to_streamed_response_wrapper(
            conferences.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            conferences.update,
        )
        self.retrieve_conferences = async_to_streamed_response_wrapper(
            conferences.retrieve_conferences,
        )
        self.retrieve_recordings = async_to_streamed_response_wrapper(
            conferences.retrieve_recordings,
        )
        self.retrieve_recordings_json = async_to_streamed_response_wrapper(
            conferences.retrieve_recordings_json,
        )

    @cached_property
    def participants(self) -> AsyncParticipantsResourceWithStreamingResponse:
        return AsyncParticipantsResourceWithStreamingResponse(self._conferences.participants)
