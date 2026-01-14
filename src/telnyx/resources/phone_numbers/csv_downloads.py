# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ...types.phone_numbers import csv_download_list_params, csv_download_create_params
from ...types.phone_numbers.csv_download import CsvDownload
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
        csv_format: Literal["V1", "V2"] | Omit = omit,
        filter: csv_download_create_params.Filter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[CsvDownload]:
        """
        List CSV downloads

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/phone_numbers/csv_downloads",
            page=SyncDefaultFlatPagination[CsvDownload],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    csv_download_list_params.CsvDownloadListParams,
                ),
            ),
            model=CsvDownload,
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
        csv_format: Literal["V1", "V2"] | Omit = omit,
        filter: csv_download_create_params.Filter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
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

    def list(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CsvDownload, AsyncDefaultFlatPagination[CsvDownload]]:
        """
        List CSV downloads

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/phone_numbers/csv_downloads",
            page=AsyncDefaultFlatPagination[CsvDownload],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    csv_download_list_params.CsvDownloadListParams,
                ),
            ),
            model=CsvDownload,
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
