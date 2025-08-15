# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.phone_numbers import (
    action_enable_emergency_params,
    action_verify_ownership_params,
    action_change_bundle_status_params,
)
from ...types.phone_numbers.action_enable_emergency_response import ActionEnableEmergencyResponse
from ...types.phone_numbers.action_verify_ownership_response import ActionVerifyOwnershipResponse
from ...types.phone_numbers.action_change_bundle_status_response import ActionChangeBundleStatusResponse

__all__ = ["ActionsResource", "AsyncActionsResource"]


class ActionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return ActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return ActionsResourceWithStreamingResponse(self)

    def change_bundle_status(
        self,
        id: str,
        *,
        bundle_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeBundleStatusResponse:
        """
        Change the bundle status for a phone number (set to being in a bundle or remove
        from a bundle)

        Args:
          bundle_id: The new bundle_id setting for the number. If you are assigning the number to a
              bundle, this is the unique ID of the bundle you wish to use. If you are removing
              the number from a bundle, this must be null. You cannot assign a number from one
              bundle to another directly. You must first remove it from a bundle, and then
              assign it to a new bundle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/phone_numbers/{id}/actions/bundle_status_change",
            body=maybe_transform(
                {"bundle_id": bundle_id}, action_change_bundle_status_params.ActionChangeBundleStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeBundleStatusResponse,
        )

    def enable_emergency(
        self,
        id: str,
        *,
        emergency_address_id: str,
        emergency_enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnableEmergencyResponse:
        """
        Enable emergency for a phone number

        Args:
          emergency_address_id: Identifies the address to be used with emergency services.

          emergency_enabled: Indicates whether to enable emergency services on this number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/phone_numbers/{id}/actions/enable_emergency",
            body=maybe_transform(
                {
                    "emergency_address_id": emergency_address_id,
                    "emergency_enabled": emergency_enabled,
                },
                action_enable_emergency_params.ActionEnableEmergencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnableEmergencyResponse,
        )

    def verify_ownership(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionVerifyOwnershipResponse:
        """
        Verifies ownership of the provided phone numbers and returns a mapping of
        numbers to their IDs, plus a list of numbers not found in the account.

        Args:
          phone_numbers: Array of phone numbers to verify ownership for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/phone_numbers/actions/verify_ownership",
            body=maybe_transform(
                {"phone_numbers": phone_numbers}, action_verify_ownership_params.ActionVerifyOwnershipParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionVerifyOwnershipResponse,
        )


class AsyncActionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncActionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncActionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncActionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncActionsResourceWithStreamingResponse(self)

    async def change_bundle_status(
        self,
        id: str,
        *,
        bundle_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionChangeBundleStatusResponse:
        """
        Change the bundle status for a phone number (set to being in a bundle or remove
        from a bundle)

        Args:
          bundle_id: The new bundle_id setting for the number. If you are assigning the number to a
              bundle, this is the unique ID of the bundle you wish to use. If you are removing
              the number from a bundle, this must be null. You cannot assign a number from one
              bundle to another directly. You must first remove it from a bundle, and then
              assign it to a new bundle.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/phone_numbers/{id}/actions/bundle_status_change",
            body=await async_maybe_transform(
                {"bundle_id": bundle_id}, action_change_bundle_status_params.ActionChangeBundleStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionChangeBundleStatusResponse,
        )

    async def enable_emergency(
        self,
        id: str,
        *,
        emergency_address_id: str,
        emergency_enabled: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionEnableEmergencyResponse:
        """
        Enable emergency for a phone number

        Args:
          emergency_address_id: Identifies the address to be used with emergency services.

          emergency_enabled: Indicates whether to enable emergency services on this number.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/phone_numbers/{id}/actions/enable_emergency",
            body=await async_maybe_transform(
                {
                    "emergency_address_id": emergency_address_id,
                    "emergency_enabled": emergency_enabled,
                },
                action_enable_emergency_params.ActionEnableEmergencyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionEnableEmergencyResponse,
        )

    async def verify_ownership(
        self,
        *,
        phone_numbers: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionVerifyOwnershipResponse:
        """
        Verifies ownership of the provided phone numbers and returns a mapping of
        numbers to their IDs, plus a list of numbers not found in the account.

        Args:
          phone_numbers: Array of phone numbers to verify ownership for

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/phone_numbers/actions/verify_ownership",
            body=await async_maybe_transform(
                {"phone_numbers": phone_numbers}, action_verify_ownership_params.ActionVerifyOwnershipParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ActionVerifyOwnershipResponse,
        )


class ActionsResourceWithRawResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.change_bundle_status = to_raw_response_wrapper(
            actions.change_bundle_status,
        )
        self.enable_emergency = to_raw_response_wrapper(
            actions.enable_emergency,
        )
        self.verify_ownership = to_raw_response_wrapper(
            actions.verify_ownership,
        )


class AsyncActionsResourceWithRawResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.change_bundle_status = async_to_raw_response_wrapper(
            actions.change_bundle_status,
        )
        self.enable_emergency = async_to_raw_response_wrapper(
            actions.enable_emergency,
        )
        self.verify_ownership = async_to_raw_response_wrapper(
            actions.verify_ownership,
        )


class ActionsResourceWithStreamingResponse:
    def __init__(self, actions: ActionsResource) -> None:
        self._actions = actions

        self.change_bundle_status = to_streamed_response_wrapper(
            actions.change_bundle_status,
        )
        self.enable_emergency = to_streamed_response_wrapper(
            actions.enable_emergency,
        )
        self.verify_ownership = to_streamed_response_wrapper(
            actions.verify_ownership,
        )


class AsyncActionsResourceWithStreamingResponse:
    def __init__(self, actions: AsyncActionsResource) -> None:
        self._actions = actions

        self.change_bundle_status = async_to_streamed_response_wrapper(
            actions.change_bundle_status,
        )
        self.enable_emergency = async_to_streamed_response_wrapper(
            actions.enable_emergency,
        )
        self.verify_ownership = async_to_streamed_response_wrapper(
            actions.verify_ownership,
        )
