# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
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
from ...types.external_connections import upload_list_params, upload_create_params
from ...types.external_connections.upload_list_response import UploadListResponse
from ...types.external_connections.upload_retry_response import UploadRetryResponse
from ...types.external_connections.upload_create_response import UploadCreateResponse
from ...types.external_connections.upload_retrieve_response import UploadRetrieveResponse
from ...types.external_connections.upload_pending_count_response import UploadPendingCountResponse
from ...types.external_connections.upload_refresh_status_response import UploadRefreshStatusResponse

__all__ = ["UploadsResource", "AsyncUploadsResource"]


class UploadsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return UploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return UploadsResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        number_ids: List[str],
        additional_usages: List[Literal["calling_user_assignment", "first_party_app_assignment"]]
        | NotGiven = NOT_GIVEN,
        civic_address_id: str | NotGiven = NOT_GIVEN,
        location_id: str | NotGiven = NOT_GIVEN,
        usage: Literal["calling_user_assignment", "first_party_app_assignment"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadCreateResponse:
        """
        Creates a new Upload request to Microsoft teams with the included phone numbers.
        Only one of civic_address_id or location_id must be provided, not both. The
        maximum allowed phone numbers for the numbers_ids array is 1000.

        Args:
          civic_address_id: Identifies the civic address to assign all phone numbers to.

          location_id: Identifies the location to assign all phone numbers to.

          usage: The use case of the upload request. NOTE: `calling_user_assignment` is not
              supported for toll free numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/external_connections/{id}/uploads",
            body=maybe_transform(
                {
                    "number_ids": number_ids,
                    "additional_usages": additional_usages,
                    "civic_address_id": civic_address_id,
                    "location_id": location_id,
                    "usage": usage,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateResponse,
        )

    def retrieve(
        self,
        ticket_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadRetrieveResponse:
        """
        Return the details of an Upload request and its phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ticket_id:
            raise ValueError(f"Expected a non-empty value for `ticket_id` but received {ticket_id!r}")
        return self._get(
            f"/external_connections/{id}/uploads/{ticket_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadRetrieveResponse,
        )

    def list(
        self,
        id: str,
        *,
        filter: upload_list_params.Filter | NotGiven = NOT_GIVEN,
        page: upload_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadListResponse:
        """
        Returns a list of your Upload requests for the given external connection.

        Args:
          filter: Filter parameter for uploads (deepObject style). Supports filtering by status,
              civic_address_id, location_id, and phone_number with eq/contains operations.

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
            f"/external_connections/{id}/uploads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    upload_list_params.UploadListParams,
                ),
            ),
            cast_to=UploadListResponse,
        )

    def pending_count(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadPendingCountResponse:
        """
        Returns the count of all pending upload requests for the given external
        connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/external_connections/{id}/uploads/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadPendingCountResponse,
        )

    def refresh_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadRefreshStatusResponse:
        """
        Forces a recheck of the status of all pending Upload requests for the given
        external connection in the background.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/external_connections/{id}/uploads/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadRefreshStatusResponse,
        )

    def retry(
        self,
        ticket_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadRetryResponse:
        """
        If there were any errors during the upload process, this endpoint will retry the
        upload request. In some cases this will reattempt the existing upload request,
        in other cases it may create a new upload request. Please check the ticket_id in
        the response to determine if a new upload request was created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ticket_id:
            raise ValueError(f"Expected a non-empty value for `ticket_id` but received {ticket_id!r}")
        return self._post(
            f"/external_connections/{id}/uploads/{ticket_id}/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadRetryResponse,
        )


class AsyncUploadsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUploadsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUploadsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUploadsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncUploadsResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        number_ids: List[str],
        additional_usages: List[Literal["calling_user_assignment", "first_party_app_assignment"]]
        | NotGiven = NOT_GIVEN,
        civic_address_id: str | NotGiven = NOT_GIVEN,
        location_id: str | NotGiven = NOT_GIVEN,
        usage: Literal["calling_user_assignment", "first_party_app_assignment"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadCreateResponse:
        """
        Creates a new Upload request to Microsoft teams with the included phone numbers.
        Only one of civic_address_id or location_id must be provided, not both. The
        maximum allowed phone numbers for the numbers_ids array is 1000.

        Args:
          civic_address_id: Identifies the civic address to assign all phone numbers to.

          location_id: Identifies the location to assign all phone numbers to.

          usage: The use case of the upload request. NOTE: `calling_user_assignment` is not
              supported for toll free numbers.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/external_connections/{id}/uploads",
            body=await async_maybe_transform(
                {
                    "number_ids": number_ids,
                    "additional_usages": additional_usages,
                    "civic_address_id": civic_address_id,
                    "location_id": location_id,
                    "usage": usage,
                },
                upload_create_params.UploadCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadCreateResponse,
        )

    async def retrieve(
        self,
        ticket_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadRetrieveResponse:
        """
        Return the details of an Upload request and its phone numbers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ticket_id:
            raise ValueError(f"Expected a non-empty value for `ticket_id` but received {ticket_id!r}")
        return await self._get(
            f"/external_connections/{id}/uploads/{ticket_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadRetrieveResponse,
        )

    async def list(
        self,
        id: str,
        *,
        filter: upload_list_params.Filter | NotGiven = NOT_GIVEN,
        page: upload_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadListResponse:
        """
        Returns a list of your Upload requests for the given external connection.

        Args:
          filter: Filter parameter for uploads (deepObject style). Supports filtering by status,
              civic_address_id, location_id, and phone_number with eq/contains operations.

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
            f"/external_connections/{id}/uploads",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "page": page,
                    },
                    upload_list_params.UploadListParams,
                ),
            ),
            cast_to=UploadListResponse,
        )

    async def pending_count(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadPendingCountResponse:
        """
        Returns the count of all pending upload requests for the given external
        connection.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/external_connections/{id}/uploads/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadPendingCountResponse,
        )

    async def refresh_status(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadRefreshStatusResponse:
        """
        Forces a recheck of the status of all pending Upload requests for the given
        external connection in the background.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/external_connections/{id}/uploads/refresh",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadRefreshStatusResponse,
        )

    async def retry(
        self,
        ticket_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UploadRetryResponse:
        """
        If there were any errors during the upload process, this endpoint will retry the
        upload request. In some cases this will reattempt the existing upload request,
        in other cases it may create a new upload request. Please check the ticket_id in
        the response to determine if a new upload request was created.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not ticket_id:
            raise ValueError(f"Expected a non-empty value for `ticket_id` but received {ticket_id!r}")
        return await self._post(
            f"/external_connections/{id}/uploads/{ticket_id}/retry",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UploadRetryResponse,
        )


class UploadsResourceWithRawResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_raw_response_wrapper(
            uploads.create,
        )
        self.retrieve = to_raw_response_wrapper(
            uploads.retrieve,
        )
        self.list = to_raw_response_wrapper(
            uploads.list,
        )
        self.pending_count = to_raw_response_wrapper(
            uploads.pending_count,
        )
        self.refresh_status = to_raw_response_wrapper(
            uploads.refresh_status,
        )
        self.retry = to_raw_response_wrapper(
            uploads.retry,
        )


class AsyncUploadsResourceWithRawResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_raw_response_wrapper(
            uploads.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            uploads.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            uploads.list,
        )
        self.pending_count = async_to_raw_response_wrapper(
            uploads.pending_count,
        )
        self.refresh_status = async_to_raw_response_wrapper(
            uploads.refresh_status,
        )
        self.retry = async_to_raw_response_wrapper(
            uploads.retry,
        )


class UploadsResourceWithStreamingResponse:
    def __init__(self, uploads: UploadsResource) -> None:
        self._uploads = uploads

        self.create = to_streamed_response_wrapper(
            uploads.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            uploads.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            uploads.list,
        )
        self.pending_count = to_streamed_response_wrapper(
            uploads.pending_count,
        )
        self.refresh_status = to_streamed_response_wrapper(
            uploads.refresh_status,
        )
        self.retry = to_streamed_response_wrapper(
            uploads.retry,
        )


class AsyncUploadsResourceWithStreamingResponse:
    def __init__(self, uploads: AsyncUploadsResource) -> None:
        self._uploads = uploads

        self.create = async_to_streamed_response_wrapper(
            uploads.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            uploads.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            uploads.list,
        )
        self.pending_count = async_to_streamed_response_wrapper(
            uploads.pending_count,
        )
        self.refresh_status = async_to_streamed_response_wrapper(
            uploads.refresh_status,
        )
        self.retry = async_to_streamed_response_wrapper(
            uploads.retry,
        )
