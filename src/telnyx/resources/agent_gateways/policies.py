# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

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
from ...types.agent_gateways import (
    policy_create_params,
    policy_update_params,
)
from ...types.agent_gateways.policy_list_response import PolicyListResponse
from ...types.agent_gateways.agent_gateway_policy_response import AgentGatewayPolicyResponse
from ...types.agent_gateways.agent_gateway_policy_pipeline_param import AgentGatewayPolicyPipelineParam
from ...types.agent_gateways.agent_gateway_policy_guardrails_param import AgentGatewayPolicyGuardrailsParam

__all__ = ["PoliciesResource", "AsyncPoliciesResource"]


class PoliciesResource(SyncAPIResource):
    """Named sets of guardrails an instance applies to requests."""

    @cached_property
    def with_raw_response(self) -> PoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PoliciesResourceWithStreamingResponse(self)

    def create(
        self,
        instance_id: str,
        *,
        name: str,
        base: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        guardrails: AgentGatewayPolicyGuardrailsParam | Omit = omit,
        model: Optional[str] | Omit = omit,
        pipeline: Optional[AgentGatewayPolicyPipelineParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyResponse:
        """Creates a named set of guardrails.

        It applies from the next request on, to the
        requests that name it in `policies` and to those its
        [attachments](https://developers.telnyx.com/api-reference/agent-gateway-policy-attachments/attach-a-policy)
        match.

        Args:
          name: A name, unique on the instance. A request names the policy in its `policies`
              field.

          base: A policy this one builds on, by name. The policy starts with the base's
              guardrails.

          description: What the policy is for.

          guardrails: The guardrails a policy adds to its base's, and the ones it removes from them,
              by name.

          model: A condition on the model, by name or regular expression. The policy's guardrails
              run only on requests for a matching model. `null` matches every model.

          pipeline: Ordered steps that run in place of the policy's guardrails running
              independently.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template("/agent_gateways/{instance_id}/policies", instance_id=instance_id),
            body=maybe_transform(
                {
                    "name": name,
                    "base": base,
                    "description": description,
                    "guardrails": guardrails,
                    "model": model,
                    "pipeline": pipeline,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyResponse,
        )

    def retrieve(
        self,
        name: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyResponse:
        """
        Returns one policy, in its current version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/policies/{name}", instance_id=instance_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyResponse,
        )

    def update(
        self,
        name: str,
        *,
        instance_id: str,
        base: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        guardrails: AgentGatewayPolicyGuardrailsParam | Omit = omit,
        model: Optional[str] | Omit = omit,
        pipeline: Optional[AgentGatewayPolicyPipelineParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyResponse:
        """Changes a policy, which publishes a new version of it.

        A field left out stays as
        it is; `guardrails` and `pipeline` are replaced whole, and `model: null` removes
        the condition.

        Args:
          base: A policy this one builds on, by name. The policy starts with the base's
              guardrails.

          description: What the policy is for.

          guardrails: The guardrails a policy adds to its base's, and the ones it removes from them,
              by name.

          model: A condition on the model, by name or regular expression. The policy's guardrails
              run only on requests for a matching model. `null` matches every model.

          pipeline: Ordered steps that run in place of the policy's guardrails running
              independently.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._patch(
            path_template("/agent_gateways/{instance_id}/policies/{name}", instance_id=instance_id, name=name),
            body=maybe_transform(
                {
                    "base": base,
                    "description": description,
                    "guardrails": guardrails,
                    "model": model,
                    "pipeline": pipeline,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyResponse,
        )

    def list(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyListResponse:
        """
        Lists the instance's policies, each in its current version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/policies", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyListResponse,
        )

    def delete(
        self,
        name: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyResponse:
        """Deletes a policy and every version of it, and returns it as it was.

        A policy
        that an attachment names, or that another policy builds on, cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._delete(
            path_template("/agent_gateways/{instance_id}/policies/{name}", instance_id=instance_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyResponse,
        )


class AsyncPoliciesResource(AsyncAPIResource):
    """Named sets of guardrails an instance applies to requests."""

    @cached_property
    def with_raw_response(self) -> AsyncPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPoliciesResourceWithStreamingResponse(self)

    async def create(
        self,
        instance_id: str,
        *,
        name: str,
        base: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        guardrails: AgentGatewayPolicyGuardrailsParam | Omit = omit,
        model: Optional[str] | Omit = omit,
        pipeline: Optional[AgentGatewayPolicyPipelineParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyResponse:
        """Creates a named set of guardrails.

        It applies from the next request on, to the
        requests that name it in `policies` and to those its
        [attachments](https://developers.telnyx.com/api-reference/agent-gateway-policy-attachments/attach-a-policy)
        match.

        Args:
          name: A name, unique on the instance. A request names the policy in its `policies`
              field.

          base: A policy this one builds on, by name. The policy starts with the base's
              guardrails.

          description: What the policy is for.

          guardrails: The guardrails a policy adds to its base's, and the ones it removes from them,
              by name.

          model: A condition on the model, by name or regular expression. The policy's guardrails
              run only on requests for a matching model. `null` matches every model.

          pipeline: Ordered steps that run in place of the policy's guardrails running
              independently.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template("/agent_gateways/{instance_id}/policies", instance_id=instance_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "base": base,
                    "description": description,
                    "guardrails": guardrails,
                    "model": model,
                    "pipeline": pipeline,
                },
                policy_create_params.PolicyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyResponse,
        )

    async def retrieve(
        self,
        name: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyResponse:
        """
        Returns one policy, in its current version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/policies/{name}", instance_id=instance_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyResponse,
        )

    async def update(
        self,
        name: str,
        *,
        instance_id: str,
        base: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        guardrails: AgentGatewayPolicyGuardrailsParam | Omit = omit,
        model: Optional[str] | Omit = omit,
        pipeline: Optional[AgentGatewayPolicyPipelineParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyResponse:
        """Changes a policy, which publishes a new version of it.

        A field left out stays as
        it is; `guardrails` and `pipeline` are replaced whole, and `model: null` removes
        the condition.

        Args:
          base: A policy this one builds on, by name. The policy starts with the base's
              guardrails.

          description: What the policy is for.

          guardrails: The guardrails a policy adds to its base's, and the ones it removes from them,
              by name.

          model: A condition on the model, by name or regular expression. The policy's guardrails
              run only on requests for a matching model. `null` matches every model.

          pipeline: Ordered steps that run in place of the policy's guardrails running
              independently.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._patch(
            path_template("/agent_gateways/{instance_id}/policies/{name}", instance_id=instance_id, name=name),
            body=await async_maybe_transform(
                {
                    "base": base,
                    "description": description,
                    "guardrails": guardrails,
                    "model": model,
                    "pipeline": pipeline,
                },
                policy_update_params.PolicyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyResponse,
        )

    async def list(
        self,
        instance_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PolicyListResponse:
        """
        Lists the instance's policies, each in its current version.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/policies", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyListResponse,
        )

    async def delete(
        self,
        name: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyResponse:
        """Deletes a policy and every version of it, and returns it as it was.

        A policy
        that an attachment names, or that another policy builds on, cannot be deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._delete(
            path_template("/agent_gateways/{instance_id}/policies/{name}", instance_id=instance_id, name=name),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyResponse,
        )


class PoliciesResourceWithRawResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_raw_response_wrapper(
            policies.create,
        )
        self.retrieve = to_raw_response_wrapper(
            policies.retrieve,
        )
        self.update = to_raw_response_wrapper(
            policies.update,
        )
        self.list = to_raw_response_wrapper(
            policies.list,
        )
        self.delete = to_raw_response_wrapper(
            policies.delete,
        )


class AsyncPoliciesResourceWithRawResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_raw_response_wrapper(
            policies.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            policies.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            policies.update,
        )
        self.list = async_to_raw_response_wrapper(
            policies.list,
        )
        self.delete = async_to_raw_response_wrapper(
            policies.delete,
        )


class PoliciesResourceWithStreamingResponse:
    def __init__(self, policies: PoliciesResource) -> None:
        self._policies = policies

        self.create = to_streamed_response_wrapper(
            policies.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            policies.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            policies.update,
        )
        self.list = to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = to_streamed_response_wrapper(
            policies.delete,
        )


class AsyncPoliciesResourceWithStreamingResponse:
    def __init__(self, policies: AsyncPoliciesResource) -> None:
        self._policies = policies

        self.create = async_to_streamed_response_wrapper(
            policies.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            policies.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            policies.update,
        )
        self.list = async_to_streamed_response_wrapper(
            policies.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            policies.delete,
        )
