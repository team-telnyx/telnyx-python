# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.rcs.agents import test_device_create_params
from ....types.rcs.agents.test_device_response import TestDeviceResponse
from ....types.rcs.agents.test_device_list_response import TestDeviceListResponse

__all__ = ["TestDevicesResource", "AsyncTestDevicesResource"]


class TestDevicesResource(SyncAPIResource):
    __test__ = False
    """Manage RCS agent registration, testing, verification, and launch."""

    @cached_property
    def with_raw_response(self) -> TestDevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return TestDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TestDevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return TestDevicesResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestDeviceResponse:
        """Adds an RCS-capable test number after provider agent creation.

        Repeating the
        request for a number already attached to the agent returns the existing test
        device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            path_template("/rcs/agents/{id}/test_devices", id=id),
            body=maybe_transform({"phone_number": phone_number}, test_device_create_params.TestDeviceCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestDeviceResponse,
        )

    def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestDeviceListResponse:
        """
        Lists test devices attached to an RCS agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/rcs/agents/{id}/test_devices", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestDeviceListResponse,
        )

    def delete(
        self,
        test_device_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a test device from an RCS agent and its provider registration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not test_device_id:
            raise ValueError(f"Expected a non-empty value for `test_device_id` but received {test_device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/rcs/agents/{id}/test_devices/{test_device_id}", id=id, test_device_id=test_device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncTestDevicesResource(AsyncAPIResource):
    """Manage RCS agent registration, testing, verification, and launch."""

    @cached_property
    def with_raw_response(self) -> AsyncTestDevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTestDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTestDevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncTestDevicesResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        phone_number: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestDeviceResponse:
        """Adds an RCS-capable test number after provider agent creation.

        Repeating the
        request for a number already attached to the agent returns the existing test
        device.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            path_template("/rcs/agents/{id}/test_devices", id=id),
            body=await async_maybe_transform(
                {"phone_number": phone_number}, test_device_create_params.TestDeviceCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestDeviceResponse,
        )

    async def list(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TestDeviceListResponse:
        """
        Lists test devices attached to an RCS agent.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/rcs/agents/{id}/test_devices", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TestDeviceListResponse,
        )

    async def delete(
        self,
        test_device_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a test device from an RCS agent and its provider registration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not test_device_id:
            raise ValueError(f"Expected a non-empty value for `test_device_id` but received {test_device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/rcs/agents/{id}/test_devices/{test_device_id}", id=id, test_device_id=test_device_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class TestDevicesResourceWithRawResponse:
    __test__ = False

    def __init__(self, test_devices: TestDevicesResource) -> None:
        self._test_devices = test_devices

        self.create = to_raw_response_wrapper(
            test_devices.create,
        )
        self.list = to_raw_response_wrapper(
            test_devices.list,
        )
        self.delete = to_raw_response_wrapper(
            test_devices.delete,
        )


class AsyncTestDevicesResourceWithRawResponse:
    def __init__(self, test_devices: AsyncTestDevicesResource) -> None:
        self._test_devices = test_devices

        self.create = async_to_raw_response_wrapper(
            test_devices.create,
        )
        self.list = async_to_raw_response_wrapper(
            test_devices.list,
        )
        self.delete = async_to_raw_response_wrapper(
            test_devices.delete,
        )


class TestDevicesResourceWithStreamingResponse:
    __test__ = False

    def __init__(self, test_devices: TestDevicesResource) -> None:
        self._test_devices = test_devices

        self.create = to_streamed_response_wrapper(
            test_devices.create,
        )
        self.list = to_streamed_response_wrapper(
            test_devices.list,
        )
        self.delete = to_streamed_response_wrapper(
            test_devices.delete,
        )


class AsyncTestDevicesResourceWithStreamingResponse:
    def __init__(self, test_devices: AsyncTestDevicesResource) -> None:
        self._test_devices = test_devices

        self.create = async_to_streamed_response_wrapper(
            test_devices.create,
        )
        self.list = async_to_streamed_response_wrapper(
            test_devices.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            test_devices.delete,
        )
