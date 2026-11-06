# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.agent_gateways import policy_attachment_create_params
from ...types.agent_gateways.policy_attachment_list_response import PolicyAttachmentListResponse
from ...types.agent_gateways.agent_gateway_policy_attachment_response import AgentGatewayPolicyAttachmentResponse

__all__ = ["PolicyAttachmentsResource", "AsyncPolicyAttachmentsResource"]


class PolicyAttachmentsResource(SyncAPIResource):
    """Where an instance applies each policy."""

    @cached_property
    def with_raw_response(self) -> PolicyAttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return PolicyAttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PolicyAttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return PolicyAttachmentsResourceWithStreamingResponse(self)

    def create(
        self,
        instance_id: str,
        *,
        policy: str,
        default: bool | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyAttachmentResponse:
        """Applies a policy to every request, or to the requests for the models named.

        It
        applies from the next request on.

        Args:
          policy: The policy to apply, by name.

          default: `true` applies the policy only to the requests no other attachment matches.

          models: The models whose requests the policy applies to, by name. A name can use `*` as
              a wildcard. Empty applies the policy to every request.

          priority: An attachment with a priority applies before the others.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template("/agent_gateways/{instance_id}/policy_attachments", instance_id=instance_id),
            body=maybe_transform(
                {
                    "policy": policy,
                    "default": default,
                    "models": models,
                    "priority": priority,
                },
                policy_attachment_create_params.PolicyAttachmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyAttachmentResponse,
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
    ) -> PolicyAttachmentListResponse:
        """
        Lists where the instance applies each policy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/policy_attachments", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyAttachmentListResponse,
        )

    def delete(
        self,
        attachment_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyAttachmentResponse:
        """Removes an attachment and returns it as it was.

        The policy stays.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return self._delete(
            path_template(
                "/agent_gateways/{instance_id}/policy_attachments/{attachment_id}",
                instance_id=instance_id,
                attachment_id=attachment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyAttachmentResponse,
        )


class AsyncPolicyAttachmentsResource(AsyncAPIResource):
    """Where an instance applies each policy."""

    @cached_property
    def with_raw_response(self) -> AsyncPolicyAttachmentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPolicyAttachmentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPolicyAttachmentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncPolicyAttachmentsResourceWithStreamingResponse(self)

    async def create(
        self,
        instance_id: str,
        *,
        policy: str,
        default: bool | Omit = omit,
        models: SequenceNotStr[str] | Omit = omit,
        priority: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyAttachmentResponse:
        """Applies a policy to every request, or to the requests for the models named.

        It
        applies from the next request on.

        Args:
          policy: The policy to apply, by name.

          default: `true` applies the policy only to the requests no other attachment matches.

          models: The models whose requests the policy applies to, by name. A name can use `*` as
              a wildcard. Empty applies the policy to every request.

          priority: An attachment with a priority applies before the others.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template("/agent_gateways/{instance_id}/policy_attachments", instance_id=instance_id),
            body=await async_maybe_transform(
                {
                    "policy": policy,
                    "default": default,
                    "models": models,
                    "priority": priority,
                },
                policy_attachment_create_params.PolicyAttachmentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyAttachmentResponse,
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
    ) -> PolicyAttachmentListResponse:
        """
        Lists where the instance applies each policy.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/policy_attachments", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PolicyAttachmentListResponse,
        )

    async def delete(
        self,
        attachment_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayPolicyAttachmentResponse:
        """Removes an attachment and returns it as it was.

        The policy stays.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not attachment_id:
            raise ValueError(f"Expected a non-empty value for `attachment_id` but received {attachment_id!r}")
        return await self._delete(
            path_template(
                "/agent_gateways/{instance_id}/policy_attachments/{attachment_id}",
                instance_id=instance_id,
                attachment_id=attachment_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayPolicyAttachmentResponse,
        )


class PolicyAttachmentsResourceWithRawResponse:
    def __init__(self, policy_attachments: PolicyAttachmentsResource) -> None:
        self._policy_attachments = policy_attachments

        self.create = to_raw_response_wrapper(
            policy_attachments.create,
        )
        self.list = to_raw_response_wrapper(
            policy_attachments.list,
        )
        self.delete = to_raw_response_wrapper(
            policy_attachments.delete,
        )


class AsyncPolicyAttachmentsResourceWithRawResponse:
    def __init__(self, policy_attachments: AsyncPolicyAttachmentsResource) -> None:
        self._policy_attachments = policy_attachments

        self.create = async_to_raw_response_wrapper(
            policy_attachments.create,
        )
        self.list = async_to_raw_response_wrapper(
            policy_attachments.list,
        )
        self.delete = async_to_raw_response_wrapper(
            policy_attachments.delete,
        )


class PolicyAttachmentsResourceWithStreamingResponse:
    def __init__(self, policy_attachments: PolicyAttachmentsResource) -> None:
        self._policy_attachments = policy_attachments

        self.create = to_streamed_response_wrapper(
            policy_attachments.create,
        )
        self.list = to_streamed_response_wrapper(
            policy_attachments.list,
        )
        self.delete = to_streamed_response_wrapper(
            policy_attachments.delete,
        )


class AsyncPolicyAttachmentsResourceWithStreamingResponse:
    def __init__(self, policy_attachments: AsyncPolicyAttachmentsResource) -> None:
        self._policy_attachments = policy_attachments

        self.create = async_to_streamed_response_wrapper(
            policy_attachments.create,
        )
        self.list = async_to_streamed_response_wrapper(
            policy_attachments.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            policy_attachments.delete,
        )
