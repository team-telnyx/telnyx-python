# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Union, cast
from datetime import datetime
from typing_extensions import Literal

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
from ...types.compute import (
    func_retrieve_logs_params,
    func_retrieve_revisions_params,
    func_retrieve_metric_aggregates_params,
)
from ...types.compute.func_retrieve_logs_response import FuncRetrieveLogsResponse
from ...types.compute.func_retrieve_revisions_response import FuncRetrieveRevisionsResponse
from ...types.compute.func_retrieve_ship_inspection_response import FuncRetrieveShipInspectionResponse
from ...types.compute.func_retrieve_metric_aggregates_response import FuncRetrieveMetricAggregatesResponse

__all__ = ["FuncsResource", "AsyncFuncsResource"]


class FuncsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FuncsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return FuncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FuncsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return FuncsResourceWithStreamingResponse(self)

    def retrieve_logs(
        self,
        id: str,
        *,
        end_time: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        type: Literal["runtime", "invocations"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncRetrieveLogsResponse:
        """Returns logs oldest first.

        `type=runtime` (default) returns function
        stdout/stderr. `type=invocations` returns one platform-generated record per HTTP
        request served.

        Args:
          end_time: Return records at or before this RFC 3339 timestamp.

          limit: Maximum records to return.

          start_time: Return records at or after this RFC 3339 timestamp.

          type: Log stream to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            FuncRetrieveLogsResponse,
            self._get(
                path_template("/compute/funcs/{id}/logs", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "end_time": end_time,
                            "limit": limit,
                            "start_time": start_time,
                            "type": type,
                        },
                        func_retrieve_logs_params.FuncRetrieveLogsParams,
                    ),
                ),
                cast_to=cast(
                    Any, FuncRetrieveLogsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_metric_aggregates(
        self,
        id: str,
        *,
        end_time: Union[str, datetime],
        start_time: Union[str, datetime],
        filter_edge_site: str | Omit = omit,
        filter_namespace: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncRetrieveMetricAggregatesResponse:
        """
        Returns aggregate request, latency, CPU, memory, and resource-limit metrics for
        a function over the requested window.

        Args:
          end_time: Exclusive window end, UTC ISO 8601 with milliseconds

          start_time: Inclusive window start, UTC ISO 8601 with milliseconds

          filter_edge_site: Edge site filter

          filter_namespace: Kubernetes namespace filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/compute/funcs/{id}/metric_aggregates", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "filter_edge_site": filter_edge_site,
                        "filter_namespace": filter_namespace,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    func_retrieve_metric_aggregates_params.FuncRetrieveMetricAggregatesParams,
                ),
            ),
            cast_to=FuncRetrieveMetricAggregatesResponse,
        )

    def retrieve_revisions(
        self,
        id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncRetrieveRevisionsResponse:
        """
        Lists a function's ship history newest first, including per-ship failure stage
        and reason when recorded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/compute/funcs/{id}/revisions", id=id),
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
                    func_retrieve_revisions_params.FuncRetrieveRevisionsParams,
                ),
            ),
            cast_to=FuncRetrieveRevisionsResponse,
        )

    def retrieve_ship_inspection(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncRetrieveShipInspectionResponse:
        """Returns the latest ship outcome.

        The stage is `none` on success, `pending` while
        building, or a failure stage such as `build`, `platform`, `pre_build`, `deploy`,
        or `security_review`. This stage-neutral customer-facing path is an alias over
        the same inspection resource as `build_log_inspection`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/compute/funcs/{id}/ship_inspection", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FuncRetrieveShipInspectionResponse,
        )


class AsyncFuncsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFuncsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFuncsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFuncsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncFuncsResourceWithStreamingResponse(self)

    async def retrieve_logs(
        self,
        id: str,
        *,
        end_time: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        start_time: Union[str, datetime] | Omit = omit,
        type: Literal["runtime", "invocations"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncRetrieveLogsResponse:
        """Returns logs oldest first.

        `type=runtime` (default) returns function
        stdout/stderr. `type=invocations` returns one platform-generated record per HTTP
        request served.

        Args:
          end_time: Return records at or before this RFC 3339 timestamp.

          limit: Maximum records to return.

          start_time: Return records at or after this RFC 3339 timestamp.

          type: Log stream to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            FuncRetrieveLogsResponse,
            await self._get(
                path_template("/compute/funcs/{id}/logs", id=id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "end_time": end_time,
                            "limit": limit,
                            "start_time": start_time,
                            "type": type,
                        },
                        func_retrieve_logs_params.FuncRetrieveLogsParams,
                    ),
                ),
                cast_to=cast(
                    Any, FuncRetrieveLogsResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_metric_aggregates(
        self,
        id: str,
        *,
        end_time: Union[str, datetime],
        start_time: Union[str, datetime],
        filter_edge_site: str | Omit = omit,
        filter_namespace: str | Omit = omit,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncRetrieveMetricAggregatesResponse:
        """
        Returns aggregate request, latency, CPU, memory, and resource-limit metrics for
        a function over the requested window.

        Args:
          end_time: Exclusive window end, UTC ISO 8601 with milliseconds

          start_time: Inclusive window start, UTC ISO 8601 with milliseconds

          filter_edge_site: Edge site filter

          filter_namespace: Kubernetes namespace filter

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/compute/funcs/{id}/metric_aggregates", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_time": end_time,
                        "start_time": start_time,
                        "filter_edge_site": filter_edge_site,
                        "filter_namespace": filter_namespace,
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    func_retrieve_metric_aggregates_params.FuncRetrieveMetricAggregatesParams,
                ),
            ),
            cast_to=FuncRetrieveMetricAggregatesResponse,
        )

    async def retrieve_revisions(
        self,
        id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncRetrieveRevisionsResponse:
        """
        Lists a function's ship history newest first, including per-ship failure stage
        and reason when recorded.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/compute/funcs/{id}/revisions", id=id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                    },
                    func_retrieve_revisions_params.FuncRetrieveRevisionsParams,
                ),
            ),
            cast_to=FuncRetrieveRevisionsResponse,
        )

    async def retrieve_ship_inspection(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FuncRetrieveShipInspectionResponse:
        """Returns the latest ship outcome.

        The stage is `none` on success, `pending` while
        building, or a failure stage such as `build`, `platform`, `pre_build`, `deploy`,
        or `security_review`. This stage-neutral customer-facing path is an alias over
        the same inspection resource as `build_log_inspection`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/compute/funcs/{id}/ship_inspection", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FuncRetrieveShipInspectionResponse,
        )


class FuncsResourceWithRawResponse:
    def __init__(self, funcs: FuncsResource) -> None:
        self._funcs = funcs

        self.retrieve_logs = to_raw_response_wrapper(
            funcs.retrieve_logs,
        )
        self.retrieve_metric_aggregates = to_raw_response_wrapper(
            funcs.retrieve_metric_aggregates,
        )
        self.retrieve_revisions = to_raw_response_wrapper(
            funcs.retrieve_revisions,
        )
        self.retrieve_ship_inspection = to_raw_response_wrapper(
            funcs.retrieve_ship_inspection,
        )


class AsyncFuncsResourceWithRawResponse:
    def __init__(self, funcs: AsyncFuncsResource) -> None:
        self._funcs = funcs

        self.retrieve_logs = async_to_raw_response_wrapper(
            funcs.retrieve_logs,
        )
        self.retrieve_metric_aggregates = async_to_raw_response_wrapper(
            funcs.retrieve_metric_aggregates,
        )
        self.retrieve_revisions = async_to_raw_response_wrapper(
            funcs.retrieve_revisions,
        )
        self.retrieve_ship_inspection = async_to_raw_response_wrapper(
            funcs.retrieve_ship_inspection,
        )


class FuncsResourceWithStreamingResponse:
    def __init__(self, funcs: FuncsResource) -> None:
        self._funcs = funcs

        self.retrieve_logs = to_streamed_response_wrapper(
            funcs.retrieve_logs,
        )
        self.retrieve_metric_aggregates = to_streamed_response_wrapper(
            funcs.retrieve_metric_aggregates,
        )
        self.retrieve_revisions = to_streamed_response_wrapper(
            funcs.retrieve_revisions,
        )
        self.retrieve_ship_inspection = to_streamed_response_wrapper(
            funcs.retrieve_ship_inspection,
        )


class AsyncFuncsResourceWithStreamingResponse:
    def __init__(self, funcs: AsyncFuncsResource) -> None:
        self._funcs = funcs

        self.retrieve_logs = async_to_streamed_response_wrapper(
            funcs.retrieve_logs,
        )
        self.retrieve_metric_aggregates = async_to_streamed_response_wrapper(
            funcs.retrieve_metric_aggregates,
        )
        self.retrieve_revisions = async_to_streamed_response_wrapper(
            funcs.retrieve_revisions,
        )
        self.retrieve_ship_inspection = async_to_streamed_response_wrapper(
            funcs.retrieve_ship_inspection,
        )
