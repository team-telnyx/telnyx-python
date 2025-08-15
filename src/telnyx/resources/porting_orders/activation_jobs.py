# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

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
from ...types.porting_orders import activation_job_list_params, activation_job_update_params
from ...types.porting_orders.activation_job_list_response import ActivationJobListResponse
from ...types.porting_orders.activation_job_update_response import ActivationJobUpdateResponse
from ...types.porting_orders.activation_job_retrieve_response import ActivationJobRetrieveResponse

__all__ = ["ActivationJobsResource", "AsyncActivationJobsResource"]


class ActivationJobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActivationJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActivationJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActivationJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActivationJobsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        activation_job_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationJobRetrieveResponse:
        """
        Returns a porting activation job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not activation_job_id:
            raise ValueError(f"Expected a non-empty value for `activation_job_id` but received {activation_job_id!r}")
        return self._get(
            f"/porting_orders/{id}/activation_jobs/{activation_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActivationJobRetrieveResponse,
        )

    def update(
        self,
        activation_job_id: str,
        *,
        id: str,
        activate_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationJobUpdateResponse:
        """
        Updates the activation time of a porting activation job.

        Args:
          activate_at: The desired activation time. The activation time should be between any of the
              activation windows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not activation_job_id:
            raise ValueError(f"Expected a non-empty value for `activation_job_id` but received {activation_job_id!r}")
        return self._patch(
            f"/porting_orders/{id}/activation_jobs/{activation_job_id}",
            body=maybe_transform({"activate_at": activate_at}, activation_job_update_params.ActivationJobUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActivationJobUpdateResponse,
        )

    def list(
        self,
        id: str,
        *,
        page: activation_job_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationJobListResponse:
        """
        Returns a list of your porting activation jobs.

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
            f"/porting_orders/{id}/activation_jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, activation_job_list_params.ActivationJobListParams),
            ),
            cast_to=ActivationJobListResponse,
        )


class AsyncActivationJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActivationJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActivationJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActivationJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActivationJobsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        activation_job_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationJobRetrieveResponse:
        """
        Returns a porting activation job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not activation_job_id:
            raise ValueError(f"Expected a non-empty value for `activation_job_id` but received {activation_job_id!r}")
        return await self._get(
            f"/porting_orders/{id}/activation_jobs/{activation_job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActivationJobRetrieveResponse,
        )

    async def update(
        self,
        activation_job_id: str,
        *,
        id: str,
        activate_at: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationJobUpdateResponse:
        """
        Updates the activation time of a porting activation job.

        Args:
          activate_at: The desired activation time. The activation time should be between any of the
              activation windows.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not activation_job_id:
            raise ValueError(f"Expected a non-empty value for `activation_job_id` but received {activation_job_id!r}")
        return await self._patch(
            f"/porting_orders/{id}/activation_jobs/{activation_job_id}",
            body=await async_maybe_transform(
                {"activate_at": activate_at}, activation_job_update_params.ActivationJobUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActivationJobUpdateResponse,
        )

    async def list(
        self,
        id: str,
        *,
        page: activation_job_list_params.Page | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActivationJobListResponse:
        """
        Returns a list of your porting activation jobs.

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
            f"/porting_orders/{id}/activation_jobs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, activation_job_list_params.ActivationJobListParams),
            ),
            cast_to=ActivationJobListResponse,
        )


class ActivationJobsResourceWithRawResponse:
    def __init__(self, activation_jobs: ActivationJobsResource) -> None:
        self._activation_jobs = activation_jobs

        self.retrieve = to_raw_response_wrapper(
            activation_jobs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            activation_jobs.update,
        )
        self.list = to_raw_response_wrapper(
            activation_jobs.list,
        )


class AsyncActivationJobsResourceWithRawResponse:
    def __init__(self, activation_jobs: AsyncActivationJobsResource) -> None:
        self._activation_jobs = activation_jobs

        self.retrieve = async_to_raw_response_wrapper(
            activation_jobs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            activation_jobs.update,
        )
        self.list = async_to_raw_response_wrapper(
            activation_jobs.list,
        )


class ActivationJobsResourceWithStreamingResponse:
    def __init__(self, activation_jobs: ActivationJobsResource) -> None:
        self._activation_jobs = activation_jobs

        self.retrieve = to_streamed_response_wrapper(
            activation_jobs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            activation_jobs.update,
        )
        self.list = to_streamed_response_wrapper(
            activation_jobs.list,
        )


class AsyncActivationJobsResourceWithStreamingResponse:
    def __init__(self, activation_jobs: AsyncActivationJobsResource) -> None:
        self._activation_jobs = activation_jobs

        self.retrieve = async_to_streamed_response_wrapper(
            activation_jobs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            activation_jobs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            activation_jobs.list,
        )
