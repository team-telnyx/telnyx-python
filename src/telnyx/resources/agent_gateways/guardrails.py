# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
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
from ...types.agent_gateways import guardrail_create_params, guardrail_update_params
from ...types.agent_gateways.guardrail_list_response import GuardrailListResponse
from ...types.agent_gateways.agent_gateway_guardrail_response import AgentGatewayGuardrailResponse

__all__ = ["GuardrailsResource", "AsyncGuardrailsResource"]


class GuardrailsResource(SyncAPIResource):
    """Checks an instance runs on model and tool requests."""

    @cached_property
    def with_raw_response(self) -> GuardrailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return GuardrailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GuardrailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return GuardrailsResourceWithStreamingResponse(self)

    def create(
        self,
        instance_id: str,
        *,
        modes: List[
            Literal[
                "before_request",
                "during_request",
                "after_request",
                "logging_only",
                "before_tool_request",
                "during_tool_request",
                "after_tool_request",
            ]
        ],
        name: str,
        type: Literal[
            "content_filter",
            "tool_permission",
            "model_judge",
            "custom_code",
            "lakera",
            "presidio",
            "bedrock",
            "azure_content_safety",
        ],
        always_on: bool | Omit = omit,
        settings: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayGuardrailResponse:
        """Adds a check the instance runs on model and tool requests.

        It runs on every
        request when `always_on`, and otherwise on the requests that name it in
        `guardrails`. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          modes: When the guardrail runs. Each type runs in some modes only.

          name: A name, unique on the instance. A request names it in its `guardrails` field.

          type: The kind of check. It cannot change after create.

          always_on: `true` runs the guardrail on every request, and a request cannot turn it off.
              `false` runs it on the requests that name it.

          settings: The type's settings. `content_filter`: `patterns` (prebuilt patterns by `name`,
              such as `us_ssn` or `email`), `regexes` (each a `name`, which tags masked
              matches, and a `pattern`), `keywords` (each a `keyword`), and `categories` (each
              a `name`), each entry with an `action` of `block` or `mask`. `tool_permission`:
              `rules` (`id`, `tool_name`, `tool_type`, `decision`, `argument_patterns`), a
              `default` decision, and `on_denied` (`block` or `rewrite`). `model_judge`: a
              `model` on the instance and weighted `criteria` (`name`, `description`,
              `weight`, the weights summing to 100). `custom_code`: `code` defining
              `apply_guardrail(inputs, request_data, input_type)`. `lakera`: `api_key`,
              `project_id`, `api_base`. `presidio`: `analyzer_url`, `anonymizer_url`,
              `entities` (entity name to `block` or `mask`), `language`. `bedrock`:
              `guardrail_id`, `version`, `region`, and `access_key_id` with
              `secret_access_key`, or `role_name`. `azure_content_safety`: `api_key`,
              `endpoint`, `severity` (0 to 7). Provider secrets are write-only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._post(
            path_template("/agent_gateways/{instance_id}/guardrails", instance_id=instance_id),
            body=maybe_transform(
                {
                    "modes": modes,
                    "name": name,
                    "type": type,
                    "always_on": always_on,
                    "settings": settings,
                },
                guardrail_create_params.GuardrailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayGuardrailResponse,
        )

    def update(
        self,
        guardrail_id: str,
        *,
        instance_id: str,
        always_on: bool | Omit = omit,
        modes: List[
            Literal[
                "before_request",
                "during_request",
                "after_request",
                "logging_only",
                "before_tool_request",
                "during_tool_request",
                "after_tool_request",
            ]
        ]
        | Omit = omit,
        name: str | Omit = omit,
        settings: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayGuardrailResponse:
        """Changes a guardrail's `name`, `modes`, `always_on`, or `settings`.

        `settings` is
        replaced whole, secrets included. The `type` cannot change. The instance must be
        `ready`; otherwise the request answers `409`.

        Args:
          always_on: `true` runs the guardrail on every request, and a request cannot turn it off.
              `false` runs it on the requests that name it.

          modes: When the guardrail runs. Each type runs in some modes only.

          name: A name, unique on the instance. A request names it in its `guardrails` field.

          settings: The type's settings. `content_filter`: `patterns` (prebuilt patterns by name,
              such as `us_ssn` or `email`), `regexes`, `keywords`, and `categories` (such as
              `prompt_injection`), each with an `action` of `block` or `mask`.
              `tool_permission`: `rules` (`id`, `tool_name`, `tool_type`, `decision`,
              `argument_patterns`), a `default` decision, and `on_denied` (`block` or
              `rewrite`). `model_judge`: a `model` on the instance and weighted `criteria`
              (`name`, `description`, `weight`, the weights summing to 100). `custom_code`:
              `code` defining `apply_guardrail(inputs, request_data, input_type)`. `lakera`:
              `api_key`, `project_id`, `api_base`. `presidio`: `analyzer_url`,
              `anonymizer_url`, `entities` (entity name to `block` or `mask`), `language`.
              `bedrock`: `guardrail_id`, `version`, `region`, and `access_key_id` with
              `secret_access_key`, or `role_name`. `azure_content_safety`: `api_key`,
              `endpoint`, `severity` (0 to 7). Provider secrets are write-only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not guardrail_id:
            raise ValueError(f"Expected a non-empty value for `guardrail_id` but received {guardrail_id!r}")
        return self._patch(
            path_template(
                "/agent_gateways/{instance_id}/guardrails/{guardrail_id}",
                instance_id=instance_id,
                guardrail_id=guardrail_id,
            ),
            body=maybe_transform(
                {
                    "always_on": always_on,
                    "modes": modes,
                    "name": name,
                    "settings": settings,
                },
                guardrail_update_params.GuardrailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayGuardrailResponse,
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
    ) -> GuardrailListResponse:
        """Lists the instance's guardrails, without their secrets.

        The instance must be
        `ready`; otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return self._get(
            path_template("/agent_gateways/{instance_id}/guardrails", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuardrailListResponse,
        )

    def delete(
        self,
        guardrail_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayGuardrailResponse:
        """Removes a guardrail and returns it as it was.

        The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not guardrail_id:
            raise ValueError(f"Expected a non-empty value for `guardrail_id` but received {guardrail_id!r}")
        return self._delete(
            path_template(
                "/agent_gateways/{instance_id}/guardrails/{guardrail_id}",
                instance_id=instance_id,
                guardrail_id=guardrail_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayGuardrailResponse,
        )


class AsyncGuardrailsResource(AsyncAPIResource):
    """Checks an instance runs on model and tool requests."""

    @cached_property
    def with_raw_response(self) -> AsyncGuardrailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGuardrailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGuardrailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncGuardrailsResourceWithStreamingResponse(self)

    async def create(
        self,
        instance_id: str,
        *,
        modes: List[
            Literal[
                "before_request",
                "during_request",
                "after_request",
                "logging_only",
                "before_tool_request",
                "during_tool_request",
                "after_tool_request",
            ]
        ],
        name: str,
        type: Literal[
            "content_filter",
            "tool_permission",
            "model_judge",
            "custom_code",
            "lakera",
            "presidio",
            "bedrock",
            "azure_content_safety",
        ],
        always_on: bool | Omit = omit,
        settings: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayGuardrailResponse:
        """Adds a check the instance runs on model and tool requests.

        It runs on every
        request when `always_on`, and otherwise on the requests that name it in
        `guardrails`. The instance must be `ready`; otherwise the request answers `409`.

        Args:
          modes: When the guardrail runs. Each type runs in some modes only.

          name: A name, unique on the instance. A request names it in its `guardrails` field.

          type: The kind of check. It cannot change after create.

          always_on: `true` runs the guardrail on every request, and a request cannot turn it off.
              `false` runs it on the requests that name it.

          settings: The type's settings. `content_filter`: `patterns` (prebuilt patterns by `name`,
              such as `us_ssn` or `email`), `regexes` (each a `name`, which tags masked
              matches, and a `pattern`), `keywords` (each a `keyword`), and `categories` (each
              a `name`), each entry with an `action` of `block` or `mask`. `tool_permission`:
              `rules` (`id`, `tool_name`, `tool_type`, `decision`, `argument_patterns`), a
              `default` decision, and `on_denied` (`block` or `rewrite`). `model_judge`: a
              `model` on the instance and weighted `criteria` (`name`, `description`,
              `weight`, the weights summing to 100). `custom_code`: `code` defining
              `apply_guardrail(inputs, request_data, input_type)`. `lakera`: `api_key`,
              `project_id`, `api_base`. `presidio`: `analyzer_url`, `anonymizer_url`,
              `entities` (entity name to `block` or `mask`), `language`. `bedrock`:
              `guardrail_id`, `version`, `region`, and `access_key_id` with
              `secret_access_key`, or `role_name`. `azure_content_safety`: `api_key`,
              `endpoint`, `severity` (0 to 7). Provider secrets are write-only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._post(
            path_template("/agent_gateways/{instance_id}/guardrails", instance_id=instance_id),
            body=await async_maybe_transform(
                {
                    "modes": modes,
                    "name": name,
                    "type": type,
                    "always_on": always_on,
                    "settings": settings,
                },
                guardrail_create_params.GuardrailCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayGuardrailResponse,
        )

    async def update(
        self,
        guardrail_id: str,
        *,
        instance_id: str,
        always_on: bool | Omit = omit,
        modes: List[
            Literal[
                "before_request",
                "during_request",
                "after_request",
                "logging_only",
                "before_tool_request",
                "during_tool_request",
                "after_tool_request",
            ]
        ]
        | Omit = omit,
        name: str | Omit = omit,
        settings: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayGuardrailResponse:
        """Changes a guardrail's `name`, `modes`, `always_on`, or `settings`.

        `settings` is
        replaced whole, secrets included. The `type` cannot change. The instance must be
        `ready`; otherwise the request answers `409`.

        Args:
          always_on: `true` runs the guardrail on every request, and a request cannot turn it off.
              `false` runs it on the requests that name it.

          modes: When the guardrail runs. Each type runs in some modes only.

          name: A name, unique on the instance. A request names it in its `guardrails` field.

          settings: The type's settings. `content_filter`: `patterns` (prebuilt patterns by name,
              such as `us_ssn` or `email`), `regexes`, `keywords`, and `categories` (such as
              `prompt_injection`), each with an `action` of `block` or `mask`.
              `tool_permission`: `rules` (`id`, `tool_name`, `tool_type`, `decision`,
              `argument_patterns`), a `default` decision, and `on_denied` (`block` or
              `rewrite`). `model_judge`: a `model` on the instance and weighted `criteria`
              (`name`, `description`, `weight`, the weights summing to 100). `custom_code`:
              `code` defining `apply_guardrail(inputs, request_data, input_type)`. `lakera`:
              `api_key`, `project_id`, `api_base`. `presidio`: `analyzer_url`,
              `anonymizer_url`, `entities` (entity name to `block` or `mask`), `language`.
              `bedrock`: `guardrail_id`, `version`, `region`, and `access_key_id` with
              `secret_access_key`, or `role_name`. `azure_content_safety`: `api_key`,
              `endpoint`, `severity` (0 to 7). Provider secrets are write-only.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not guardrail_id:
            raise ValueError(f"Expected a non-empty value for `guardrail_id` but received {guardrail_id!r}")
        return await self._patch(
            path_template(
                "/agent_gateways/{instance_id}/guardrails/{guardrail_id}",
                instance_id=instance_id,
                guardrail_id=guardrail_id,
            ),
            body=await async_maybe_transform(
                {
                    "always_on": always_on,
                    "modes": modes,
                    "name": name,
                    "settings": settings,
                },
                guardrail_update_params.GuardrailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayGuardrailResponse,
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
    ) -> GuardrailListResponse:
        """Lists the instance's guardrails, without their secrets.

        The instance must be
        `ready`; otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        return await self._get(
            path_template("/agent_gateways/{instance_id}/guardrails", instance_id=instance_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuardrailListResponse,
        )

    async def delete(
        self,
        guardrail_id: str,
        *,
        instance_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentGatewayGuardrailResponse:
        """Removes a guardrail and returns it as it was.

        The instance must be `ready`;
        otherwise the request answers `409`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not instance_id:
            raise ValueError(f"Expected a non-empty value for `instance_id` but received {instance_id!r}")
        if not guardrail_id:
            raise ValueError(f"Expected a non-empty value for `guardrail_id` but received {guardrail_id!r}")
        return await self._delete(
            path_template(
                "/agent_gateways/{instance_id}/guardrails/{guardrail_id}",
                instance_id=instance_id,
                guardrail_id=guardrail_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentGatewayGuardrailResponse,
        )


class GuardrailsResourceWithRawResponse:
    def __init__(self, guardrails: GuardrailsResource) -> None:
        self._guardrails = guardrails

        self.create = to_raw_response_wrapper(
            guardrails.create,
        )
        self.update = to_raw_response_wrapper(
            guardrails.update,
        )
        self.list = to_raw_response_wrapper(
            guardrails.list,
        )
        self.delete = to_raw_response_wrapper(
            guardrails.delete,
        )


class AsyncGuardrailsResourceWithRawResponse:
    def __init__(self, guardrails: AsyncGuardrailsResource) -> None:
        self._guardrails = guardrails

        self.create = async_to_raw_response_wrapper(
            guardrails.create,
        )
        self.update = async_to_raw_response_wrapper(
            guardrails.update,
        )
        self.list = async_to_raw_response_wrapper(
            guardrails.list,
        )
        self.delete = async_to_raw_response_wrapper(
            guardrails.delete,
        )


class GuardrailsResourceWithStreamingResponse:
    def __init__(self, guardrails: GuardrailsResource) -> None:
        self._guardrails = guardrails

        self.create = to_streamed_response_wrapper(
            guardrails.create,
        )
        self.update = to_streamed_response_wrapper(
            guardrails.update,
        )
        self.list = to_streamed_response_wrapper(
            guardrails.list,
        )
        self.delete = to_streamed_response_wrapper(
            guardrails.delete,
        )


class AsyncGuardrailsResourceWithStreamingResponse:
    def __init__(self, guardrails: AsyncGuardrailsResource) -> None:
        self._guardrails = guardrails

        self.create = async_to_streamed_response_wrapper(
            guardrails.create,
        )
        self.update = async_to_streamed_response_wrapper(
            guardrails.update,
        )
        self.list = async_to_streamed_response_wrapper(
            guardrails.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            guardrails.delete,
        )
