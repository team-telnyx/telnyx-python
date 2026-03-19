# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Query, Headers, NotGiven, not_given
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
from ....types.whatsapp.phone_numbers import calling_setting_update_params
from ....types.whatsapp.phone_numbers.calling_setting_update_response import CallingSettingUpdateResponse
from ....types.whatsapp.phone_numbers.calling_setting_retrieve_response import CallingSettingRetrieveResponse

__all__ = ["CallingSettingsResource", "AsyncCallingSettingsResource"]


class CallingSettingsResource(SyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def with_raw_response(self) -> CallingSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return CallingSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CallingSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return CallingSettingsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallingSettingRetrieveResponse:
        """
        Get calling settings for a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._get(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/calling_settings", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallingSettingRetrieveResponse,
        )

    def update(
        self,
        phone_number: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallingSettingUpdateResponse:
        """
        Enable or disable Whatsapp calling for a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return self._patch(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/calling_settings", phone_number=phone_number),
            body=maybe_transform({"enabled": enabled}, calling_setting_update_params.CallingSettingUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallingSettingUpdateResponse,
        )


class AsyncCallingSettingsResource(AsyncAPIResource):
    """Manage Whatsapp phone numbers"""

    @cached_property
    def with_raw_response(self) -> AsyncCallingSettingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCallingSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCallingSettingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncCallingSettingsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        phone_number: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallingSettingRetrieveResponse:
        """
        Get calling settings for a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._get(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/calling_settings", phone_number=phone_number),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallingSettingRetrieveResponse,
        )

    async def update(
        self,
        phone_number: str,
        *,
        enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CallingSettingUpdateResponse:
        """
        Enable or disable Whatsapp calling for a phone number

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not phone_number:
            raise ValueError(f"Expected a non-empty value for `phone_number` but received {phone_number!r}")
        return await self._patch(
            path_template("/v2/whatsapp/phone_numbers/{phone_number}/calling_settings", phone_number=phone_number),
            body=await async_maybe_transform(
                {"enabled": enabled}, calling_setting_update_params.CallingSettingUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CallingSettingUpdateResponse,
        )


class CallingSettingsResourceWithRawResponse:
    def __init__(self, calling_settings: CallingSettingsResource) -> None:
        self._calling_settings = calling_settings

        self.retrieve = to_raw_response_wrapper(
            calling_settings.retrieve,
        )
        self.update = to_raw_response_wrapper(
            calling_settings.update,
        )


class AsyncCallingSettingsResourceWithRawResponse:
    def __init__(self, calling_settings: AsyncCallingSettingsResource) -> None:
        self._calling_settings = calling_settings

        self.retrieve = async_to_raw_response_wrapper(
            calling_settings.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            calling_settings.update,
        )


class CallingSettingsResourceWithStreamingResponse:
    def __init__(self, calling_settings: CallingSettingsResource) -> None:
        self._calling_settings = calling_settings

        self.retrieve = to_streamed_response_wrapper(
            calling_settings.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            calling_settings.update,
        )


class AsyncCallingSettingsResourceWithStreamingResponse:
    def __init__(self, calling_settings: AsyncCallingSettingsResource) -> None:
        self._calling_settings = calling_settings

        self.retrieve = async_to_streamed_response_wrapper(
            calling_settings.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            calling_settings.update,
        )
