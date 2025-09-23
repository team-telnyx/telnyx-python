# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ....._types import Body, Query, Headers, NotGiven, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.legacy.reporting.batch_detail_records import speech_to_text_create_params
from .....types.legacy.reporting.batch_detail_records.speech_to_text_list_response import SpeechToTextListResponse
from .....types.legacy.reporting.batch_detail_records.speech_to_text_create_response import SpeechToTextCreateResponse
from .....types.legacy.reporting.batch_detail_records.speech_to_text_delete_response import SpeechToTextDeleteResponse
from .....types.legacy.reporting.batch_detail_records.speech_to_text_retrieve_response import (
    SpeechToTextRetrieveResponse,
)

__all__ = ["SpeechToTextResource", "AsyncSpeechToTextResource"]


class SpeechToTextResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SpeechToTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return SpeechToTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpeechToTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return SpeechToTextResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpeechToTextCreateResponse:
        """
        Creates a new Speech to Text batch report request with the specified filters

        Args:
          end_date: End date in ISO format with timezone (date range must be up to one month)

          start_date: Start date in ISO format with timezone

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/legacy/reporting/batch_detail_records/speech_to_text",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                speech_to_text_create_params.SpeechToTextCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextCreateResponse,
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
    ) -> SpeechToTextRetrieveResponse:
        """
        Retrieves a specific Speech to Text batch report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/legacy/reporting/batch_detail_records/speech_to_text/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextRetrieveResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpeechToTextListResponse:
        """Retrieves all Speech to Text batch report requests for the authenticated user"""
        return self._get(
            "/legacy/reporting/batch_detail_records/speech_to_text",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextListResponse,
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
    ) -> SpeechToTextDeleteResponse:
        """
        Deletes a specific Speech to Text batch report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/legacy/reporting/batch_detail_records/speech_to_text/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextDeleteResponse,
        )


class AsyncSpeechToTextResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSpeechToTextResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpeechToTextResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpeechToTextResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncSpeechToTextResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpeechToTextCreateResponse:
        """
        Creates a new Speech to Text batch report request with the specified filters

        Args:
          end_date: End date in ISO format with timezone (date range must be up to one month)

          start_date: Start date in ISO format with timezone

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/legacy/reporting/batch_detail_records/speech_to_text",
            body=await async_maybe_transform(
                {
                    "end_date": end_date,
                    "start_date": start_date,
                },
                speech_to_text_create_params.SpeechToTextCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextCreateResponse,
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
    ) -> SpeechToTextRetrieveResponse:
        """
        Retrieves a specific Speech to Text batch report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/legacy/reporting/batch_detail_records/speech_to_text/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextRetrieveResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SpeechToTextListResponse:
        """Retrieves all Speech to Text batch report requests for the authenticated user"""
        return await self._get(
            "/legacy/reporting/batch_detail_records/speech_to_text",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextListResponse,
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
    ) -> SpeechToTextDeleteResponse:
        """
        Deletes a specific Speech to Text batch report request by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/legacy/reporting/batch_detail_records/speech_to_text/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SpeechToTextDeleteResponse,
        )


class SpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.create = to_raw_response_wrapper(
            speech_to_text.create,
        )
        self.retrieve = to_raw_response_wrapper(
            speech_to_text.retrieve,
        )
        self.list = to_raw_response_wrapper(
            speech_to_text.list,
        )
        self.delete = to_raw_response_wrapper(
            speech_to_text.delete,
        )


class AsyncSpeechToTextResourceWithRawResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.create = async_to_raw_response_wrapper(
            speech_to_text.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            speech_to_text.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            speech_to_text.list,
        )
        self.delete = async_to_raw_response_wrapper(
            speech_to_text.delete,
        )


class SpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: SpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.create = to_streamed_response_wrapper(
            speech_to_text.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            speech_to_text.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            speech_to_text.list,
        )
        self.delete = to_streamed_response_wrapper(
            speech_to_text.delete,
        )


class AsyncSpeechToTextResourceWithStreamingResponse:
    def __init__(self, speech_to_text: AsyncSpeechToTextResource) -> None:
        self._speech_to_text = speech_to_text

        self.create = async_to_streamed_response_wrapper(
            speech_to_text.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            speech_to_text.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            speech_to_text.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            speech_to_text.delete,
        )
