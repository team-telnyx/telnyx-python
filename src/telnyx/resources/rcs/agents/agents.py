# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....types.rcs import (
    AgentUseCase,
    agent_list_params,
    agent_create_params,
    agent_launch_params,
    agent_update_params,
)
from .test_devices import (
    TestDevicesResource,
    AsyncTestDevicesResource,
    TestDevicesResourceWithRawResponse,
    AsyncTestDevicesResourceWithRawResponse,
    TestDevicesResourceWithStreamingResponse,
    AsyncTestDevicesResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.rcs.agent_response import AgentResponse
from ....types.rcs.agent_use_case import AgentUseCase
from ....types.rcs.agent_list_response import AgentListResponse
from ....types.rcs.agent_configuration_param import AgentConfigurationParam
from ....types.rcs.agent_testing_configuration_param import AgentTestingConfigurationParam
from ....types.rcs.agent_retrieve_carrier_approvals_response import AgentRetrieveCarrierApprovalsResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    """Manage RCS agent registration, testing, verification, and launch."""

    @cached_property
    def test_devices(self) -> TestDevicesResource:
        """Manage RCS agent registration, testing, verification, and launch."""
        return TestDevicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        brand_id: str,
        configuration: AgentConfigurationParam,
        display_name: str,
        use_case: AgentUseCase,
        idempotency_key: str,
        hosting_region: Optional[str] | Omit = omit,
        profile_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Creates an editable RCS agent draft under a brand.

        The `Idempotency-Key` is
        scoped to the authenticated organization. Reusing the key with the same request
        returns the original agent, while reusing it with a different request returns a
        conflict.

        Args:
          profile_id: A Messaging Profile owned by the authenticated organization. When omitted, the
              agent inherits the brand profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return self._post(
            "/rcs/agents",
            body=maybe_transform(
                {
                    "brand_id": brand_id,
                    "configuration": configuration,
                    "display_name": display_name,
                    "use_case": use_case,
                    "hosting_region": hosting_region,
                    "profile_id": profile_id,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
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
    ) -> AgentResponse:
        """
        Retrieves an RCS agent, section statuses, test devices, carrier approvals, and
        provider capabilities.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/rcs/agents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def update(
        self,
        id: str,
        *,
        configuration: AgentConfigurationParam | Omit = omit,
        display_name: str | Omit = omit,
        hosting_region: str | Omit = omit,
        profile_id: str | Omit = omit,
        use_case: AgentUseCase | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Updates one or more fields on an agent while its status is `CREATED`.

        Submitted
        agents cannot be changed through this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/rcs/agents/{id}", id=id),
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "display_name": display_name,
                    "hosting_region": hosting_region,
                    "profile_id": profile_id,
                    "use_case": use_case,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def list(
        self,
        *,
        brand_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Lists RCS agents owned by the authenticated organization, optionally filtered by
        brand.

        Args:
          brand_id: Only return agents belonging to this brand.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/rcs/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"brand_id": brand_id}, agent_list_params.AgentListParams),
            ),
            cast_to=AgentListResponse,
        )

    def launch(
        self,
        id: str,
        *,
        campaign: agent_launch_params.Campaign,
        testing: AgentTestingConfigurationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Adds the campaign and testing configuration, then starts asynchronous carrier
        launch. Agent basics must already be submitted. Repeating a launch that is
        already in progress returns the current agent without creating new work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/rcs/agents/{id}/launch", id=id),
            body=maybe_transform(
                {
                    "campaign": campaign,
                    "testing": testing,
                },
                agent_launch_params.AgentLaunchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    def retrieve_carrier_approvals(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveCarrierApprovalsResponse:
        """Lists carrier approval records for an RCS agent.

        The provider may expose
        per-carrier, hub-level, or bot-level approval status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/rcs/agents/{id}/carrier_approvals", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveCarrierApprovalsResponse,
        )

    def submit(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Starts asynchronous provider provisioning and submits the agent's basic
        configuration. The brand must be `VERIFIED`. Repeating this request for an
        in-progress agent returns its current state without creating new work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/rcs/agents/{id}/submit", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    """Manage RCS agent registration, testing, verification, and launch."""

    @cached_property
    def test_devices(self) -> AsyncTestDevicesResource:
        """Manage RCS agent registration, testing, verification, and launch."""
        return AsyncTestDevicesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        brand_id: str,
        configuration: AgentConfigurationParam,
        display_name: str,
        use_case: AgentUseCase,
        idempotency_key: str,
        hosting_region: Optional[str] | Omit = omit,
        profile_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Creates an editable RCS agent draft under a brand.

        The `Idempotency-Key` is
        scoped to the authenticated organization. Reusing the key with the same request
        returns the original agent, while reusing it with a different request returns a
        conflict.

        Args:
          profile_id: A Messaging Profile owned by the authenticated organization. When omitted, the
              agent inherits the brand profile.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Idempotency-Key": idempotency_key, **(extra_headers or {})}
        return await self._post(
            "/rcs/agents",
            body=await async_maybe_transform(
                {
                    "brand_id": brand_id,
                    "configuration": configuration,
                    "display_name": display_name,
                    "use_case": use_case,
                    "hosting_region": hosting_region,
                    "profile_id": profile_id,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
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
    ) -> AgentResponse:
        """
        Retrieves an RCS agent, section statuses, test devices, carrier approvals, and
        provider capabilities.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/rcs/agents/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def update(
        self,
        id: str,
        *,
        configuration: AgentConfigurationParam | Omit = omit,
        display_name: str | Omit = omit,
        hosting_region: str | Omit = omit,
        profile_id: str | Omit = omit,
        use_case: AgentUseCase | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """Updates one or more fields on an agent while its status is `CREATED`.

        Submitted
        agents cannot be changed through this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/rcs/agents/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "display_name": display_name,
                    "hosting_region": hosting_region,
                    "profile_id": profile_id,
                    "use_case": use_case,
                },
                agent_update_params.AgentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def list(
        self,
        *,
        brand_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentListResponse:
        """
        Lists RCS agents owned by the authenticated organization, optionally filtered by
        brand.

        Args:
          brand_id: Only return agents belonging to this brand.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/rcs/agents",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"brand_id": brand_id}, agent_list_params.AgentListParams),
            ),
            cast_to=AgentListResponse,
        )

    async def launch(
        self,
        id: str,
        *,
        campaign: agent_launch_params.Campaign,
        testing: AgentTestingConfigurationParam,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Adds the campaign and testing configuration, then starts asynchronous carrier
        launch. Agent basics must already be submitted. Repeating a launch that is
        already in progress returns the current agent without creating new work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/rcs/agents/{id}/launch", id=id),
            body=await async_maybe_transform(
                {
                    "campaign": campaign,
                    "testing": testing,
                },
                agent_launch_params.AgentLaunchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )

    async def retrieve_carrier_approvals(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentRetrieveCarrierApprovalsResponse:
        """Lists carrier approval records for an RCS agent.

        The provider may expose
        per-carrier, hub-level, or bot-level approval status.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/rcs/agents/{id}/carrier_approvals", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveCarrierApprovalsResponse,
        )

    async def submit(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentResponse:
        """
        Starts asynchronous provider provisioning and submits the agent's basic
        configuration. The brand must be `VERIFIED`. Repeating this request for an
        in-progress agent returns its current state without creating new work.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/rcs/agents/{id}/submit", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = to_raw_response_wrapper(
            agents.update,
        )
        self.list = to_raw_response_wrapper(
            agents.list,
        )
        self.launch = to_raw_response_wrapper(
            agents.launch,
        )
        self.retrieve_carrier_approvals = to_raw_response_wrapper(
            agents.retrieve_carrier_approvals,
        )
        self.submit = to_raw_response_wrapper(
            agents.submit,
        )

    @cached_property
    def test_devices(self) -> TestDevicesResourceWithRawResponse:
        """Manage RCS agent registration, testing, verification, and launch."""
        return TestDevicesResourceWithRawResponse(self._agents.test_devices)


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            agents.update,
        )
        self.list = async_to_raw_response_wrapper(
            agents.list,
        )
        self.launch = async_to_raw_response_wrapper(
            agents.launch,
        )
        self.retrieve_carrier_approvals = async_to_raw_response_wrapper(
            agents.retrieve_carrier_approvals,
        )
        self.submit = async_to_raw_response_wrapper(
            agents.submit,
        )

    @cached_property
    def test_devices(self) -> AsyncTestDevicesResourceWithRawResponse:
        """Manage RCS agent registration, testing, verification, and launch."""
        return AsyncTestDevicesResourceWithRawResponse(self._agents.test_devices)


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            agents.update,
        )
        self.list = to_streamed_response_wrapper(
            agents.list,
        )
        self.launch = to_streamed_response_wrapper(
            agents.launch,
        )
        self.retrieve_carrier_approvals = to_streamed_response_wrapper(
            agents.retrieve_carrier_approvals,
        )
        self.submit = to_streamed_response_wrapper(
            agents.submit,
        )

    @cached_property
    def test_devices(self) -> TestDevicesResourceWithStreamingResponse:
        """Manage RCS agent registration, testing, verification, and launch."""
        return TestDevicesResourceWithStreamingResponse(self._agents.test_devices)


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            agents.update,
        )
        self.list = async_to_streamed_response_wrapper(
            agents.list,
        )
        self.launch = async_to_streamed_response_wrapper(
            agents.launch,
        )
        self.retrieve_carrier_approvals = async_to_streamed_response_wrapper(
            agents.retrieve_carrier_approvals,
        )
        self.submit = async_to_streamed_response_wrapper(
            agents.submit,
        )

    @cached_property
    def test_devices(self) -> AsyncTestDevicesResourceWithStreamingResponse:
        """Manage RCS agent registration, testing, verification, and launch."""
        return AsyncTestDevicesResourceWithStreamingResponse(self._agents.test_devices)
