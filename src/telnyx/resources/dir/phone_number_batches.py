# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.dir import DirPhoneNumberStatus, phone_number_batch_list_params
from ...pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.dir.phone_number_batch import PhoneNumberBatch
from ...types.dir.dir_phone_number_status import DirPhoneNumberStatus
from ...types.dir.phone_number_batch_retrieve_response import PhoneNumberBatchRetrieveResponse

__all__ = ["PhoneNumberBatchesResource", "AsyncPhoneNumberBatchesResource"]


class PhoneNumberBatchesResource(SyncAPIResource):
    """Phone numbers are submitted to Telnyx for vetting in batches.

    Batches group all numbers added in a single request under the same Letter of Authorization.
    """

    @cached_property
    def with_raw_response(self) -> PhoneNumberBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PhoneNumberBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhoneNumberBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PhoneNumberBatchesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        batch_id: str,
        *,
        dir_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberBatchRetrieveResponse:
        """Get a single phone-number batch by id.

        The enterprise is resolved server-side
        from the DIR id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            path_template("/dir/{dir_id}/phone_number_batches/{batch_id}", dir_id=dir_id, batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberBatchRetrieveResponse,
        )

    def list(
        self,
        dir_id: str,
        *,
        filter_status: DirPhoneNumberStatus | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[PhoneNumberBatch]:
        """List the phone-number batches submitted under a DIR.

        The enterprise is resolved
        server-side from the DIR id.

        Args:
          filter_status: Restrict to batches whose aggregate status equals this value.

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._get_api_list(
            path_template("/dir/{dir_id}/phone_number_batches", dir_id=dir_id),
            page=SyncDefaultFlatPagination[PhoneNumberBatch],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_status": filter_status,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    phone_number_batch_list_params.PhoneNumberBatchListParams,
                ),
            ),
            model=PhoneNumberBatch,
        )


class AsyncPhoneNumberBatchesResource(AsyncAPIResource):
    """Phone numbers are submitted to Telnyx for vetting in batches.

    Batches group all numbers added in a single request under the same Letter of Authorization.
    """

    @cached_property
    def with_raw_response(self) -> AsyncPhoneNumberBatchesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPhoneNumberBatchesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhoneNumberBatchesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPhoneNumberBatchesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        batch_id: str,
        *,
        dir_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PhoneNumberBatchRetrieveResponse:
        """Get a single phone-number batch by id.

        The enterprise is resolved server-side
        from the DIR id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            path_template("/dir/{dir_id}/phone_number_batches/{batch_id}", dir_id=dir_id, batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PhoneNumberBatchRetrieveResponse,
        )

    def list(
        self,
        dir_id: str,
        *,
        filter_status: DirPhoneNumberStatus | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[PhoneNumberBatch, AsyncDefaultFlatPagination[PhoneNumberBatch]]:
        """List the phone-number batches submitted under a DIR.

        The enterprise is resolved
        server-side from the DIR id.

        Args:
          filter_status: Restrict to batches whose aggregate status equals this value.

          page_number: 1-based page number. Out-of-range values return an empty page with correct meta.

          page_size: Items per page. Maximum 250; values above are clamped to 250.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not dir_id:
            raise ValueError(f"Expected a non-empty value for `dir_id` but received {dir_id!r}")
        return self._get_api_list(
            path_template("/dir/{dir_id}/phone_number_batches", dir_id=dir_id),
            page=AsyncDefaultFlatPagination[PhoneNumberBatch],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter_status": filter_status,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    phone_number_batch_list_params.PhoneNumberBatchListParams,
                ),
            ),
            model=PhoneNumberBatch,
        )


class PhoneNumberBatchesResourceWithRawResponse:
    def __init__(self, phone_number_batches: PhoneNumberBatchesResource) -> None:
        self._phone_number_batches = phone_number_batches

        self.retrieve = to_raw_response_wrapper(
            phone_number_batches.retrieve,
        )
        self.list = to_raw_response_wrapper(
            phone_number_batches.list,
        )


class AsyncPhoneNumberBatchesResourceWithRawResponse:
    def __init__(self, phone_number_batches: AsyncPhoneNumberBatchesResource) -> None:
        self._phone_number_batches = phone_number_batches

        self.retrieve = async_to_raw_response_wrapper(
            phone_number_batches.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            phone_number_batches.list,
        )


class PhoneNumberBatchesResourceWithStreamingResponse:
    def __init__(self, phone_number_batches: PhoneNumberBatchesResource) -> None:
        self._phone_number_batches = phone_number_batches

        self.retrieve = to_streamed_response_wrapper(
            phone_number_batches.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            phone_number_batches.list,
        )


class AsyncPhoneNumberBatchesResourceWithStreamingResponse:
    def __init__(self, phone_number_batches: AsyncPhoneNumberBatchesResource) -> None:
        self._phone_number_batches = phone_number_batches

        self.retrieve = async_to_streamed_response_wrapper(
            phone_number_batches.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            phone_number_batches.list,
        )
