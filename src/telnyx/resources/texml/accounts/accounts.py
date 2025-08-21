# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .calls.calls import (
    CallsResource,
    AsyncCallsResource,
    CallsResourceWithRawResponse,
    AsyncCallsResourceWithRawResponse,
    CallsResourceWithStreamingResponse,
    AsyncCallsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.texml import account_retrieve_recordings_json_params, account_retrieve_transcriptions_json_params
from ...._base_client import make_request_options
from .recordings.recordings import (
    RecordingsResource,
    AsyncRecordingsResource,
    RecordingsResourceWithRawResponse,
    AsyncRecordingsResourceWithRawResponse,
    RecordingsResourceWithStreamingResponse,
    AsyncRecordingsResourceWithStreamingResponse,
)
from .conferences.conferences import (
    ConferencesResource,
    AsyncConferencesResource,
    ConferencesResourceWithRawResponse,
    AsyncConferencesResourceWithRawResponse,
    ConferencesResourceWithStreamingResponse,
    AsyncConferencesResourceWithStreamingResponse,
)
from .transcriptions.transcriptions import (
    TranscriptionsResource,
    AsyncTranscriptionsResource,
    TranscriptionsResourceWithRawResponse,
    AsyncTranscriptionsResourceWithRawResponse,
    TranscriptionsResourceWithStreamingResponse,
    AsyncTranscriptionsResourceWithStreamingResponse,
)
from ....types.texml.account_retrieve_recordings_json_response import AccountRetrieveRecordingsJsonResponse
from ....types.texml.account_retrieve_transcriptions_json_response import AccountRetrieveTranscriptionsJsonResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def calls(self) -> CallsResource:
        return CallsResource(self._client)

    @cached_property
    def conferences(self) -> ConferencesResource:
        return ConferencesResource(self._client)

    @cached_property
    def recordings(self) -> RecordingsResource:
        return RecordingsResource(self._client)

    @cached_property
    def transcriptions(self) -> TranscriptionsResource:
        return TranscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def retrieve_recordings_json(
        self,
        account_sid: str,
        *,
        date_created: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveRecordingsJsonResponse:
        """
        Returns multiple recording resources for an account.

        Args:
          date_created: Filters recording by the creation date. Expected format is ISO8601 date or
              date-time, ie. {YYYY}-{MM}-{DD} or {YYYY}-{MM}-{DD}T{hh}:{mm}:{ss}Z. Also
              accepts inequality operators, e.g. DateCreated>=2023-05-22.

          page: The number of the page to be displayed, zero-indexed, should be used in
              conjuction with PageToken.

          page_size: The number of records to be displayed on a page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Recordings.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date_created": date_created,
                        "page": page,
                        "page_size": page_size,
                    },
                    account_retrieve_recordings_json_params.AccountRetrieveRecordingsJsonParams,
                ),
            ),
            cast_to=AccountRetrieveRecordingsJsonResponse,
        )

    def retrieve_transcriptions_json(
        self,
        account_sid: str,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveTranscriptionsJsonResponse:
        """
        Returns multiple recording transcription resources for an account.

        Args:
          page_size: The number of records to be displayed on a page

          page_token: Used to request the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return self._get(
            f"/texml/Accounts/{account_sid}/Transcriptions.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    account_retrieve_transcriptions_json_params.AccountRetrieveTranscriptionsJsonParams,
                ),
            ),
            cast_to=AccountRetrieveTranscriptionsJsonResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def calls(self) -> AsyncCallsResource:
        return AsyncCallsResource(self._client)

    @cached_property
    def conferences(self) -> AsyncConferencesResource:
        return AsyncConferencesResource(self._client)

    @cached_property
    def recordings(self) -> AsyncRecordingsResource:
        return AsyncRecordingsResource(self._client)

    @cached_property
    def transcriptions(self) -> AsyncTranscriptionsResource:
        return AsyncTranscriptionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def retrieve_recordings_json(
        self,
        account_sid: str,
        *,
        date_created: Union[str, datetime] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveRecordingsJsonResponse:
        """
        Returns multiple recording resources for an account.

        Args:
          date_created: Filters recording by the creation date. Expected format is ISO8601 date or
              date-time, ie. {YYYY}-{MM}-{DD} or {YYYY}-{MM}-{DD}T{hh}:{mm}:{ss}Z. Also
              accepts inequality operators, e.g. DateCreated>=2023-05-22.

          page: The number of the page to be displayed, zero-indexed, should be used in
              conjuction with PageToken.

          page_size: The number of records to be displayed on a page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Recordings.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date_created": date_created,
                        "page": page,
                        "page_size": page_size,
                    },
                    account_retrieve_recordings_json_params.AccountRetrieveRecordingsJsonParams,
                ),
            ),
            cast_to=AccountRetrieveRecordingsJsonResponse,
        )

    async def retrieve_transcriptions_json(
        self,
        account_sid: str,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveTranscriptionsJsonResponse:
        """
        Returns multiple recording transcription resources for an account.

        Args:
          page_size: The number of records to be displayed on a page

          page_token: Used to request the next page of results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_sid:
            raise ValueError(f"Expected a non-empty value for `account_sid` but received {account_sid!r}")
        return await self._get(
            f"/texml/Accounts/{account_sid}/Transcriptions.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    account_retrieve_transcriptions_json_params.AccountRetrieveTranscriptionsJsonParams,
                ),
            ),
            cast_to=AccountRetrieveTranscriptionsJsonResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve_recordings_json = to_raw_response_wrapper(
            accounts.retrieve_recordings_json,
        )
        self.retrieve_transcriptions_json = to_raw_response_wrapper(
            accounts.retrieve_transcriptions_json,
        )

    @cached_property
    def calls(self) -> CallsResourceWithRawResponse:
        return CallsResourceWithRawResponse(self._accounts.calls)

    @cached_property
    def conferences(self) -> ConferencesResourceWithRawResponse:
        return ConferencesResourceWithRawResponse(self._accounts.conferences)

    @cached_property
    def recordings(self) -> RecordingsResourceWithRawResponse:
        return RecordingsResourceWithRawResponse(self._accounts.recordings)

    @cached_property
    def transcriptions(self) -> TranscriptionsResourceWithRawResponse:
        return TranscriptionsResourceWithRawResponse(self._accounts.transcriptions)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve_recordings_json = async_to_raw_response_wrapper(
            accounts.retrieve_recordings_json,
        )
        self.retrieve_transcriptions_json = async_to_raw_response_wrapper(
            accounts.retrieve_transcriptions_json,
        )

    @cached_property
    def calls(self) -> AsyncCallsResourceWithRawResponse:
        return AsyncCallsResourceWithRawResponse(self._accounts.calls)

    @cached_property
    def conferences(self) -> AsyncConferencesResourceWithRawResponse:
        return AsyncConferencesResourceWithRawResponse(self._accounts.conferences)

    @cached_property
    def recordings(self) -> AsyncRecordingsResourceWithRawResponse:
        return AsyncRecordingsResourceWithRawResponse(self._accounts.recordings)

    @cached_property
    def transcriptions(self) -> AsyncTranscriptionsResourceWithRawResponse:
        return AsyncTranscriptionsResourceWithRawResponse(self._accounts.transcriptions)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve_recordings_json = to_streamed_response_wrapper(
            accounts.retrieve_recordings_json,
        )
        self.retrieve_transcriptions_json = to_streamed_response_wrapper(
            accounts.retrieve_transcriptions_json,
        )

    @cached_property
    def calls(self) -> CallsResourceWithStreamingResponse:
        return CallsResourceWithStreamingResponse(self._accounts.calls)

    @cached_property
    def conferences(self) -> ConferencesResourceWithStreamingResponse:
        return ConferencesResourceWithStreamingResponse(self._accounts.conferences)

    @cached_property
    def recordings(self) -> RecordingsResourceWithStreamingResponse:
        return RecordingsResourceWithStreamingResponse(self._accounts.recordings)

    @cached_property
    def transcriptions(self) -> TranscriptionsResourceWithStreamingResponse:
        return TranscriptionsResourceWithStreamingResponse(self._accounts.transcriptions)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve_recordings_json = async_to_streamed_response_wrapper(
            accounts.retrieve_recordings_json,
        )
        self.retrieve_transcriptions_json = async_to_streamed_response_wrapper(
            accounts.retrieve_transcriptions_json,
        )

    @cached_property
    def calls(self) -> AsyncCallsResourceWithStreamingResponse:
        return AsyncCallsResourceWithStreamingResponse(self._accounts.calls)

    @cached_property
    def conferences(self) -> AsyncConferencesResourceWithStreamingResponse:
        return AsyncConferencesResourceWithStreamingResponse(self._accounts.conferences)

    @cached_property
    def recordings(self) -> AsyncRecordingsResourceWithStreamingResponse:
        return AsyncRecordingsResourceWithStreamingResponse(self._accounts.recordings)

    @cached_property
    def transcriptions(self) -> AsyncTranscriptionsResourceWithStreamingResponse:
        return AsyncTranscriptionsResourceWithStreamingResponse(self._accounts.transcriptions)
