# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal

import httpx

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
from ....._base_client import make_request_options
from .....types.ai.missions.runs import plan_create_params, plan_update_step_params, plan_add_steps_to_plan_params
from .....types.ai.missions.runs.plan_create_response import PlanCreateResponse
from .....types.ai.missions.runs.plan_retrieve_response import PlanRetrieveResponse
from .....types.ai.missions.runs.plan_update_step_response import PlanUpdateStepResponse
from .....types.ai.missions.runs.plan_get_step_details_response import PlanGetStepDetailsResponse
from .....types.ai.missions.runs.plan_add_steps_to_plan_response import PlanAddStepsToPlanResponse

__all__ = ["PlanResource", "AsyncPlanResource"]


class PlanResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PlanResourceWithStreamingResponse(self)

    def create(
        self,
        run_id: str,
        *,
        mission_id: str,
        steps: Iterable[plan_create_params.Step],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanCreateResponse:
        """
        Create the initial plan for a run

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
            f"/ai/missions/{mission_id}/runs/{run_id}/plan",
            body=maybe_transform({"steps": steps}, plan_create_params.PlanCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanCreateResponse,
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
    ) -> PlanRetrieveResponse:
        """
        Get the plan (all steps) for a run

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
            f"/ai/missions/{mission_id}/runs/{run_id}/plan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanRetrieveResponse,
        )

    def add_steps_to_plan(
        self,
        run_id: str,
        *,
        mission_id: str,
        steps: Iterable[plan_add_steps_to_plan_params.Step],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanAddStepsToPlanResponse:
        """
        Add one or more steps to an existing plan

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
            f"/ai/missions/{mission_id}/runs/{run_id}/plan/steps",
            body=maybe_transform({"steps": steps}, plan_add_steps_to_plan_params.PlanAddStepsToPlanParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanAddStepsToPlanResponse,
        )

    def get_step_details(
        self,
        step_id: str,
        *,
        mission_id: str,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanGetStepDetailsResponse:
        """
        Get details of a specific plan step

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
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._get(
            f"/ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanGetStepDetailsResponse,
        )

    def update_step(
        self,
        step_id: str,
        *,
        mission_id: str,
        run_id: str,
        metadata: Dict[str, object] | Omit = omit,
        status: Literal["pending", "in_progress", "completed", "skipped", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanUpdateStepResponse:
        """
        Update the status of a plan step

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
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return self._patch(
            f"/ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}",
            body=maybe_transform(
                {
                    "metadata": metadata,
                    "status": status,
                },
                plan_update_step_params.PlanUpdateStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanUpdateStepResponse,
        )


class AsyncPlanResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPlanResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPlanResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlanResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPlanResourceWithStreamingResponse(self)

    async def create(
        self,
        run_id: str,
        *,
        mission_id: str,
        steps: Iterable[plan_create_params.Step],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanCreateResponse:
        """
        Create the initial plan for a run

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
            f"/ai/missions/{mission_id}/runs/{run_id}/plan",
            body=await async_maybe_transform({"steps": steps}, plan_create_params.PlanCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanCreateResponse,
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
    ) -> PlanRetrieveResponse:
        """
        Get the plan (all steps) for a run

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
            f"/ai/missions/{mission_id}/runs/{run_id}/plan",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanRetrieveResponse,
        )

    async def add_steps_to_plan(
        self,
        run_id: str,
        *,
        mission_id: str,
        steps: Iterable[plan_add_steps_to_plan_params.Step],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanAddStepsToPlanResponse:
        """
        Add one or more steps to an existing plan

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
            f"/ai/missions/{mission_id}/runs/{run_id}/plan/steps",
            body=await async_maybe_transform({"steps": steps}, plan_add_steps_to_plan_params.PlanAddStepsToPlanParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanAddStepsToPlanResponse,
        )

    async def get_step_details(
        self,
        step_id: str,
        *,
        mission_id: str,
        run_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanGetStepDetailsResponse:
        """
        Get details of a specific plan step

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
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._get(
            f"/ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanGetStepDetailsResponse,
        )

    async def update_step(
        self,
        step_id: str,
        *,
        mission_id: str,
        run_id: str,
        metadata: Dict[str, object] | Omit = omit,
        status: Literal["pending", "in_progress", "completed", "skipped", "failed"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PlanUpdateStepResponse:
        """
        Update the status of a plan step

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
        if not step_id:
            raise ValueError(f"Expected a non-empty value for `step_id` but received {step_id!r}")
        return await self._patch(
            f"/ai/missions/{mission_id}/runs/{run_id}/plan/steps/{step_id}",
            body=await async_maybe_transform(
                {
                    "metadata": metadata,
                    "status": status,
                },
                plan_update_step_params.PlanUpdateStepParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PlanUpdateStepResponse,
        )


class PlanResourceWithRawResponse:
    def __init__(self, plan: PlanResource) -> None:
        self._plan = plan

        self.create = to_raw_response_wrapper(
            plan.create,
        )
        self.retrieve = to_raw_response_wrapper(
            plan.retrieve,
        )
        self.add_steps_to_plan = to_raw_response_wrapper(
            plan.add_steps_to_plan,
        )
        self.get_step_details = to_raw_response_wrapper(
            plan.get_step_details,
        )
        self.update_step = to_raw_response_wrapper(
            plan.update_step,
        )


class AsyncPlanResourceWithRawResponse:
    def __init__(self, plan: AsyncPlanResource) -> None:
        self._plan = plan

        self.create = async_to_raw_response_wrapper(
            plan.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            plan.retrieve,
        )
        self.add_steps_to_plan = async_to_raw_response_wrapper(
            plan.add_steps_to_plan,
        )
        self.get_step_details = async_to_raw_response_wrapper(
            plan.get_step_details,
        )
        self.update_step = async_to_raw_response_wrapper(
            plan.update_step,
        )


class PlanResourceWithStreamingResponse:
    def __init__(self, plan: PlanResource) -> None:
        self._plan = plan

        self.create = to_streamed_response_wrapper(
            plan.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            plan.retrieve,
        )
        self.add_steps_to_plan = to_streamed_response_wrapper(
            plan.add_steps_to_plan,
        )
        self.get_step_details = to_streamed_response_wrapper(
            plan.get_step_details,
        )
        self.update_step = to_streamed_response_wrapper(
            plan.update_step,
        )


class AsyncPlanResourceWithStreamingResponse:
    def __init__(self, plan: AsyncPlanResource) -> None:
        self._plan = plan

        self.create = async_to_streamed_response_wrapper(
            plan.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            plan.retrieve,
        )
        self.add_steps_to_plan = async_to_streamed_response_wrapper(
            plan.add_steps_to_plan,
        )
        self.get_step_details = async_to_streamed_response_wrapper(
            plan.get_step_details,
        )
        self.update_step = async_to_streamed_response_wrapper(
            plan.update_step,
        )
