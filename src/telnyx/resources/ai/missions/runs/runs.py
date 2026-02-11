# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from .plan import (
    PlanResource,
    AsyncPlanResource,
    PlanResourceWithRawResponse,
    AsyncPlanResourceWithRawResponse,
    PlanResourceWithStreamingResponse,
    AsyncPlanResourceWithStreamingResponse,
)
from .events import (
    EventsResource,
    AsyncEventsResource,
    EventsResourceWithRawResponse,
    AsyncEventsResourceWithRawResponse,
    EventsResourceWithStreamingResponse,
    AsyncEventsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .telnyx_agents import (
    TelnyxAgentsResource,
    AsyncTelnyxAgentsResource,
    TelnyxAgentsResourceWithRawResponse,
    AsyncTelnyxAgentsResourceWithRawResponse,
    TelnyxAgentsResourceWithStreamingResponse,
    AsyncTelnyxAgentsResourceWithStreamingResponse,
)
from .....pagination import SyncDefaultFlatPagination, AsyncDefaultFlatPagination
from ....._base_client import AsyncPaginator, make_request_options
from .....types.ai.missions import run_list_params, run_create_params, run_update_params, run_list_runs_params
from .....types.ai.missions.run_list_response import RunListResponse
from .....types.ai.missions.run_create_response import RunCreateResponse
from .....types.ai.missions.run_update_response import RunUpdateResponse
from .....types.ai.missions.run_retrieve_response import RunRetrieveResponse
from .....types.ai.missions.run_list_runs_response import RunListRunsResponse
from .....types.ai.missions.run_pause_run_response import RunPauseRunResponse
from .....types.ai.missions.run_cancel_run_response import RunCancelRunResponse
from .....types.ai.missions.run_resume_run_response import RunResumeRunResponse

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def events(self) -> EventsResource:
        return EventsResource(self._client)

    @cached_property
    def plan(self) -> PlanResource:
        return PlanResource(self._client)

    @cached_property
    def telnyx_agents(self) -> TelnyxAgentsResource:
        return TelnyxAgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def create(
        self,
        mission_id: str,
        *,
        input: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """
        Start a new run for a mission

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return self._post(
            f"/ai/missions/{mission_id}/runs",
            body=maybe_transform(
                {
                    "input": input,
                    "metadata": metadata,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    def retrieve(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveResponse:
        """
        Get details of a specific run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            f"/ai/missions/{mission_id}/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunRetrieveResponse,
        )

    def update(
        self,
        run_id: str,
        *,
        mission_id: str,
        error: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        result_payload: Dict[str, object] | Omit = omit,
        result_summary: str | Omit = omit,
        status: Literal["pending", "running", "paused", "succeeded", "failed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunUpdateResponse:
        """
        Update run status and/or result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._patch(
            f"/ai/missions/{mission_id}/runs/{run_id}",
            body=maybe_transform(
                {
                    "error": error,
                    "metadata": metadata,
                    "result_payload": result_payload,
                    "result_summary": result_summary,
                    "status": status,
                },
                run_update_params.RunUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunUpdateResponse,
        )

    def list(
        self,
        mission_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[RunListResponse]:
        """
        List all runs for a specific mission

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return self._get_api_list(
            f"/ai/missions/{mission_id}/runs",
            page=SyncDefaultFlatPagination[RunListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            model=RunListResponse,
        )

    def cancel_run(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCancelRunResponse:
        """
        Cancel a running or paused run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            f"/ai/missions/{mission_id}/runs/{run_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCancelRunResponse,
        )

    def list_runs(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncDefaultFlatPagination[RunListRunsResponse]:
        """
        List recent runs across all missions

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/missions/runs",
            page=SyncDefaultFlatPagination[RunListRunsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    run_list_runs_params.RunListRunsParams,
                ),
            ),
            model=RunListRunsResponse,
        )

    def pause_run(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunPauseRunResponse:
        """
        Pause a running run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            f"/ai/missions/{mission_id}/runs/{run_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunPauseRunResponse,
        )

    def resume_run(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunResumeRunResponse:
        """
        Resume a paused run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._post(
            f"/ai/missions/{mission_id}/runs/{run_id}/resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunResumeRunResponse,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def events(self) -> AsyncEventsResource:
        return AsyncEventsResource(self._client)

    @cached_property
    def plan(self) -> AsyncPlanResource:
        return AsyncPlanResource(self._client)

    @cached_property
    def telnyx_agents(self) -> AsyncTelnyxAgentsResource:
        return AsyncTelnyxAgentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        mission_id: str,
        *,
        input: Dict[str, object] | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """
        Start a new run for a mission

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return await self._post(
            f"/ai/missions/{mission_id}/runs",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "metadata": metadata,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    async def retrieve(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunRetrieveResponse:
        """
        Get details of a specific run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            f"/ai/missions/{mission_id}/runs/{run_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunRetrieveResponse,
        )

    async def update(
        self,
        run_id: str,
        *,
        mission_id: str,
        error: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        result_payload: Dict[str, object] | Omit = omit,
        result_summary: str | Omit = omit,
        status: Literal["pending", "running", "paused", "succeeded", "failed", "cancelled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunUpdateResponse:
        """
        Update run status and/or result

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._patch(
            f"/ai/missions/{mission_id}/runs/{run_id}",
            body=await async_maybe_transform(
                {
                    "error": error,
                    "metadata": metadata,
                    "result_payload": result_payload,
                    "result_summary": result_summary,
                    "status": status,
                },
                run_update_params.RunUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunUpdateResponse,
        )

    def list(
        self,
        mission_id: str,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RunListResponse, AsyncDefaultFlatPagination[RunListResponse]]:
        """
        List all runs for a specific mission

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        return self._get_api_list(
            f"/ai/missions/{mission_id}/runs",
            page=AsyncDefaultFlatPagination[RunListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    run_list_params.RunListParams,
                ),
            ),
            model=RunListResponse,
        )

    async def cancel_run(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCancelRunResponse:
        """
        Cancel a running or paused run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            f"/ai/missions/{mission_id}/runs/{run_id}/cancel",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCancelRunResponse,
        )

    def list_runs(
        self,
        *,
        page_number: int | Omit = omit,
        page_size: int | Omit = omit,
        status: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RunListRunsResponse, AsyncDefaultFlatPagination[RunListRunsResponse]]:
        """
        List recent runs across all missions

        Args:
          page_number: Page number (1-based)

          page_size: Number of items per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/ai/missions/runs",
            page=AsyncDefaultFlatPagination[RunListRunsResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_number": page_number,
                        "page_size": page_size,
                        "status": status,
                    },
                    run_list_runs_params.RunListRunsParams,
                ),
            ),
            model=RunListRunsResponse,
        )

    async def pause_run(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunPauseRunResponse:
        """
        Pause a running run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            f"/ai/missions/{mission_id}/runs/{run_id}/pause",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunPauseRunResponse,
        )

    async def resume_run(
        self,
        run_id: str,
        *,
        mission_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunResumeRunResponse:
        """
        Resume a paused run

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not mission_id:
            raise ValueError(f"Expected a non-empty value for `mission_id` but received {mission_id!r}")
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._post(
            f"/ai/missions/{mission_id}/runs/{run_id}/resume",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunResumeRunResponse,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            runs.update,
        )
        self.list = to_raw_response_wrapper(
            runs.list,
        )
        self.cancel_run = to_raw_response_wrapper(
            runs.cancel_run,
        )
        self.list_runs = to_raw_response_wrapper(
            runs.list_runs,
        )
        self.pause_run = to_raw_response_wrapper(
            runs.pause_run,
        )
        self.resume_run = to_raw_response_wrapper(
            runs.resume_run,
        )

    @cached_property
    def events(self) -> EventsResourceWithRawResponse:
        return EventsResourceWithRawResponse(self._runs.events)

    @cached_property
    def plan(self) -> PlanResourceWithRawResponse:
        return PlanResourceWithRawResponse(self._runs.plan)

    @cached_property
    def telnyx_agents(self) -> TelnyxAgentsResourceWithRawResponse:
        return TelnyxAgentsResourceWithRawResponse(self._runs.telnyx_agents)


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            runs.update,
        )
        self.list = async_to_raw_response_wrapper(
            runs.list,
        )
        self.cancel_run = async_to_raw_response_wrapper(
            runs.cancel_run,
        )
        self.list_runs = async_to_raw_response_wrapper(
            runs.list_runs,
        )
        self.pause_run = async_to_raw_response_wrapper(
            runs.pause_run,
        )
        self.resume_run = async_to_raw_response_wrapper(
            runs.resume_run,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithRawResponse:
        return AsyncEventsResourceWithRawResponse(self._runs.events)

    @cached_property
    def plan(self) -> AsyncPlanResourceWithRawResponse:
        return AsyncPlanResourceWithRawResponse(self._runs.plan)

    @cached_property
    def telnyx_agents(self) -> AsyncTelnyxAgentsResourceWithRawResponse:
        return AsyncTelnyxAgentsResourceWithRawResponse(self._runs.telnyx_agents)


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            runs.update,
        )
        self.list = to_streamed_response_wrapper(
            runs.list,
        )
        self.cancel_run = to_streamed_response_wrapper(
            runs.cancel_run,
        )
        self.list_runs = to_streamed_response_wrapper(
            runs.list_runs,
        )
        self.pause_run = to_streamed_response_wrapper(
            runs.pause_run,
        )
        self.resume_run = to_streamed_response_wrapper(
            runs.resume_run,
        )

    @cached_property
    def events(self) -> EventsResourceWithStreamingResponse:
        return EventsResourceWithStreamingResponse(self._runs.events)

    @cached_property
    def plan(self) -> PlanResourceWithStreamingResponse:
        return PlanResourceWithStreamingResponse(self._runs.plan)

    @cached_property
    def telnyx_agents(self) -> TelnyxAgentsResourceWithStreamingResponse:
        return TelnyxAgentsResourceWithStreamingResponse(self._runs.telnyx_agents)


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            runs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            runs.list,
        )
        self.cancel_run = async_to_streamed_response_wrapper(
            runs.cancel_run,
        )
        self.list_runs = async_to_streamed_response_wrapper(
            runs.list_runs,
        )
        self.pause_run = async_to_streamed_response_wrapper(
            runs.pause_run,
        )
        self.resume_run = async_to_streamed_response_wrapper(
            runs.resume_run,
        )

    @cached_property
    def events(self) -> AsyncEventsResourceWithStreamingResponse:
        return AsyncEventsResourceWithStreamingResponse(self._runs.events)

    @cached_property
    def plan(self) -> AsyncPlanResourceWithStreamingResponse:
        return AsyncPlanResourceWithStreamingResponse(self._runs.plan)

    @cached_property
    def telnyx_agents(self) -> AsyncTelnyxAgentsResourceWithStreamingResponse:
        return AsyncTelnyxAgentsResourceWithStreamingResponse(self._runs.telnyx_agents)
