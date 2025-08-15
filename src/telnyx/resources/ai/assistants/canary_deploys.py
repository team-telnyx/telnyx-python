# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.assistants import canary_deploy_create_params, canary_deploy_update_params
from ....types.ai.assistants.version_config_param import VersionConfigParam
from ....types.ai.assistants.canary_deploy_response import CanaryDeployResponse

__all__ = ["CanaryDeploysResource", "AsyncCanaryDeploysResource"]


class CanaryDeploysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CanaryDeploysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CanaryDeploysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CanaryDeploysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CanaryDeploysResourceWithStreamingResponse(self)

    def create(
        self,
        assistant_id: str,
        *,
        versions: Iterable[VersionConfigParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CanaryDeployResponse:
        """
        Endpoint to create a canary deploy configuration for an assistant.

        Creates a new canary deploy configuration with multiple version IDs and their
        traffic percentages for A/B testing or gradual rollouts of assistant versions.

        Args:
          versions: List of version configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._post(
            f"/ai/assistants/{assistant_id}/canary-deploys",
            body=maybe_transform({"versions": versions}, canary_deploy_create_params.CanaryDeployCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CanaryDeployResponse,
        )

    def retrieve(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CanaryDeployResponse:
        """
        Endpoint to get a canary deploy configuration for an assistant.

        Retrieves the current canary deploy configuration with all version IDs and their
        traffic percentages for the specified assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._get(
            f"/ai/assistants/{assistant_id}/canary-deploys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CanaryDeployResponse,
        )

    def update(
        self,
        assistant_id: str,
        *,
        versions: Iterable[VersionConfigParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CanaryDeployResponse:
        """
        Endpoint to update a canary deploy configuration for an assistant.

        Updates the existing canary deploy configuration with new version IDs and
        percentages. All old versions and percentages are replaces by new ones from this
        request.

        Args:
          versions: List of version configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return self._put(
            f"/ai/assistants/{assistant_id}/canary-deploys",
            body=maybe_transform({"versions": versions}, canary_deploy_update_params.CanaryDeployUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CanaryDeployResponse,
        )

    def delete(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Endpoint to delete a canary deploy configuration for an assistant.

        Removes all canary deploy configurations for the specified assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/ai/assistants/{assistant_id}/canary-deploys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncCanaryDeploysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCanaryDeploysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCanaryDeploysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCanaryDeploysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCanaryDeploysResourceWithStreamingResponse(self)

    async def create(
        self,
        assistant_id: str,
        *,
        versions: Iterable[VersionConfigParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CanaryDeployResponse:
        """
        Endpoint to create a canary deploy configuration for an assistant.

        Creates a new canary deploy configuration with multiple version IDs and their
        traffic percentages for A/B testing or gradual rollouts of assistant versions.

        Args:
          versions: List of version configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._post(
            f"/ai/assistants/{assistant_id}/canary-deploys",
            body=await async_maybe_transform(
                {"versions": versions}, canary_deploy_create_params.CanaryDeployCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CanaryDeployResponse,
        )

    async def retrieve(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CanaryDeployResponse:
        """
        Endpoint to get a canary deploy configuration for an assistant.

        Retrieves the current canary deploy configuration with all version IDs and their
        traffic percentages for the specified assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._get(
            f"/ai/assistants/{assistant_id}/canary-deploys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CanaryDeployResponse,
        )

    async def update(
        self,
        assistant_id: str,
        *,
        versions: Iterable[VersionConfigParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CanaryDeployResponse:
        """
        Endpoint to update a canary deploy configuration for an assistant.

        Updates the existing canary deploy configuration with new version IDs and
        percentages. All old versions and percentages are replaces by new ones from this
        request.

        Args:
          versions: List of version configurations

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        return await self._put(
            f"/ai/assistants/{assistant_id}/canary-deploys",
            body=await async_maybe_transform(
                {"versions": versions}, canary_deploy_update_params.CanaryDeployUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CanaryDeployResponse,
        )

    async def delete(
        self,
        assistant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Endpoint to delete a canary deploy configuration for an assistant.

        Removes all canary deploy configurations for the specified assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not assistant_id:
            raise ValueError(f"Expected a non-empty value for `assistant_id` but received {assistant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/ai/assistants/{assistant_id}/canary-deploys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class CanaryDeploysResourceWithRawResponse:
    def __init__(self, canary_deploys: CanaryDeploysResource) -> None:
        self._canary_deploys = canary_deploys

        self.create = to_raw_response_wrapper(
            canary_deploys.create,
        )
        self.retrieve = to_raw_response_wrapper(
            canary_deploys.retrieve,
        )
        self.update = to_raw_response_wrapper(
            canary_deploys.update,
        )
        self.delete = to_raw_response_wrapper(
            canary_deploys.delete,
        )


class AsyncCanaryDeploysResourceWithRawResponse:
    def __init__(self, canary_deploys: AsyncCanaryDeploysResource) -> None:
        self._canary_deploys = canary_deploys

        self.create = async_to_raw_response_wrapper(
            canary_deploys.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            canary_deploys.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            canary_deploys.update,
        )
        self.delete = async_to_raw_response_wrapper(
            canary_deploys.delete,
        )


class CanaryDeploysResourceWithStreamingResponse:
    def __init__(self, canary_deploys: CanaryDeploysResource) -> None:
        self._canary_deploys = canary_deploys

        self.create = to_streamed_response_wrapper(
            canary_deploys.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            canary_deploys.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            canary_deploys.update,
        )
        self.delete = to_streamed_response_wrapper(
            canary_deploys.delete,
        )


class AsyncCanaryDeploysResourceWithStreamingResponse:
    def __init__(self, canary_deploys: AsyncCanaryDeploysResource) -> None:
        self._canary_deploys = canary_deploys

        self.create = async_to_streamed_response_wrapper(
            canary_deploys.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            canary_deploys.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            canary_deploys.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            canary_deploys.delete,
        )
