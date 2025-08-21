# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

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
from ...types.actions import register_create_params
from ...types.actions.register_create_response import RegisterCreateResponse

__all__ = ["RegisterResource", "AsyncRegisterResource"]


class RegisterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegisterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return RegisterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegisterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return RegisterResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        registration_codes: List[str],
        sim_card_group_id: str | NotGiven = NOT_GIVEN,
        status: Literal["enabled", "disabled", "standby"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegisterCreateResponse:
        """
        Register the SIM cards associated with the provided registration codes to the
        current user's account.<br/><br/> If <code>sim_card_group_id</code> is provided,
        the SIM cards will be associated with that group. Otherwise, the default group
        for the current user will be used.<br/><br/>

        Args:
          sim_card_group_id: The group SIMCardGroup identification. This attribute can be <code>null</code>
              when it's present in an associated resource.

          status: Status on which the SIM card will be set after being successful registered.

          tags: Searchable tags associated with the SIM card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/actions/register/sim_cards",
            body=maybe_transform(
                {
                    "registration_codes": registration_codes,
                    "sim_card_group_id": sim_card_group_id,
                    "status": status,
                    "tags": tags,
                },
                register_create_params.RegisterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegisterCreateResponse,
        )


class AsyncRegisterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegisterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegisterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegisterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/team-telnyx/telnyx-python#with_streaming_response
        """
        return AsyncRegisterResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        registration_codes: List[str],
        sim_card_group_id: str | NotGiven = NOT_GIVEN,
        status: Literal["enabled", "disabled", "standby"] | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegisterCreateResponse:
        """
        Register the SIM cards associated with the provided registration codes to the
        current user's account.<br/><br/> If <code>sim_card_group_id</code> is provided,
        the SIM cards will be associated with that group. Otherwise, the default group
        for the current user will be used.<br/><br/>

        Args:
          sim_card_group_id: The group SIMCardGroup identification. This attribute can be <code>null</code>
              when it's present in an associated resource.

          status: Status on which the SIM card will be set after being successful registered.

          tags: Searchable tags associated with the SIM card

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/actions/register/sim_cards",
            body=await async_maybe_transform(
                {
                    "registration_codes": registration_codes,
                    "sim_card_group_id": sim_card_group_id,
                    "status": status,
                    "tags": tags,
                },
                register_create_params.RegisterCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegisterCreateResponse,
        )


class RegisterResourceWithRawResponse:
    def __init__(self, register: RegisterResource) -> None:
        self._register = register

        self.create = to_raw_response_wrapper(
            register.create,
        )


class AsyncRegisterResourceWithRawResponse:
    def __init__(self, register: AsyncRegisterResource) -> None:
        self._register = register

        self.create = async_to_raw_response_wrapper(
            register.create,
        )


class RegisterResourceWithStreamingResponse:
    def __init__(self, register: RegisterResource) -> None:
        self._register = register

        self.create = to_streamed_response_wrapper(
            register.create,
        )


class AsyncRegisterResourceWithStreamingResponse:
    def __init__(self, register: AsyncRegisterResource) -> None:
        self._register = register

        self.create = async_to_streamed_response_wrapper(
            register.create,
        )
