# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.phone_numbers import csv_download_list_params, csv_download_create_params
from ...types.phone_numbers.csv_download_list_response import CsvDownloadListResponse
from ...types.phone_numbers.csv_download_create_response import CsvDownloadCreateResponse
from ...types.phone_numbers.csv_download_retrieve_response import CsvDownloadRetrieveResponse

__all__ = ["CsvDownloadsResource", "AsyncCsvDownloadsResource"]


class CsvDownloadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CsvDownloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CsvDownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CsvDownloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CsvDownloadsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        csv_format: Literal["V1", "V2"] | NotGiven = NOT_GIVEN,
        filter: csv_download_create_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CsvDownloadCreateResponse:
        """
        Create a CSV download

        Args:
          csv_format: Which format to use when generating the CSV file. The default for backwards
              compatibility is 'V1'

          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[has_bundle], filter[tag], filter[connection_id], filter[phone_number],
              filter[status], filter[voice.connection_name],
              filter[voice.usage_payment_method], filter[billing_group_id],
              filter[emergency_address_id], filter[customer_reference]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/phone_numbers/csv_downloads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "csv_format": csv_format,
                        "filter": filter,
                    },
                    csv_download_create_params.CsvDownloadCreateParams,
                ),
            ),
            cast_to=CsvDownloadCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CsvDownloadRetrieveResponse:
        """
        Retrieve a CSV download

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/phone_numbers/csv_downloads/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CsvDownloadRetrieveResponse,
        )

    def list(
        self,
        *,
        page: csv_download_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CsvDownloadListResponse:
        """List CSV downloads

        Args:
          page: Consolidated page parameter (deepObject style).

        Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/phone_numbers/csv_downloads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, csv_download_list_params.CsvDownloadListParams),
            ),
            cast_to=CsvDownloadListResponse,
        )


class AsyncCsvDownloadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCsvDownloadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCsvDownloadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCsvDownloadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCsvDownloadsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        csv_format: Literal["V1", "V2"] | NotGiven = NOT_GIVEN,
        filter: csv_download_create_params.Filter | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CsvDownloadCreateResponse:
        """
        Create a CSV download

        Args:
          csv_format: Which format to use when generating the CSV file. The default for backwards
              compatibility is 'V1'

          filter:
              Consolidated filter parameter (deepObject style). Originally:
              filter[has_bundle], filter[tag], filter[connection_id], filter[phone_number],
              filter[status], filter[voice.connection_name],
              filter[voice.usage_payment_method], filter[billing_group_id],
              filter[emergency_address_id], filter[customer_reference]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/phone_numbers/csv_downloads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "csv_format": csv_format,
                        "filter": filter,
                    },
                    csv_download_create_params.CsvDownloadCreateParams,
                ),
            ),
            cast_to=CsvDownloadCreateResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CsvDownloadRetrieveResponse:
        """
        Retrieve a CSV download

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/phone_numbers/csv_downloads/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CsvDownloadRetrieveResponse,
        )

    async def list(
        self,
        *,
        page: csv_download_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CsvDownloadListResponse:
        """List CSV downloads

        Args:
          page: Consolidated page parameter (deepObject style).

        Originally: page[size],
              page[number]

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/phone_numbers/csv_downloads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, csv_download_list_params.CsvDownloadListParams),
            ),
            cast_to=CsvDownloadListResponse,
        )


class CsvDownloadsResourceWithRawResponse:
    def __init__(self, csv_downloads: CsvDownloadsResource) -> None:
        self._csv_downloads = csv_downloads

        self.create = to_raw_response_wrapper(
            csv_downloads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            csv_downloads.retrieve,
        )
        self.list = to_raw_response_wrapper(
            csv_downloads.list,
        )


class AsyncCsvDownloadsResourceWithRawResponse:
    def __init__(self, csv_downloads: AsyncCsvDownloadsResource) -> None:
        self._csv_downloads = csv_downloads

        self.create = async_to_raw_response_wrapper(
            csv_downloads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            csv_downloads.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            csv_downloads.list,
        )


class CsvDownloadsResourceWithStreamingResponse:
    def __init__(self, csv_downloads: CsvDownloadsResource) -> None:
        self._csv_downloads = csv_downloads

        self.create = to_streamed_response_wrapper(
            csv_downloads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            csv_downloads.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            csv_downloads.list,
        )


class AsyncCsvDownloadsResourceWithStreamingResponse:
    def __init__(self, csv_downloads: AsyncCsvDownloadsResource) -> None:
        self._csv_downloads = csv_downloads

        self.create = async_to_streamed_response_wrapper(
            csv_downloads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            csv_downloads.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            csv_downloads.list,
        )
